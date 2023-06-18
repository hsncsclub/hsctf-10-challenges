{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TemplateHaskell #-}

import Crypto.Hash.SHA256 qualified as SHA256
import Data.Bits (Bits (clearBit, testBit, xor, (.&.), (.|.)))
import Data.ByteString.Builder qualified as Builder
import Data.ByteString.Lazy qualified as B
import Data.FileEmbed (embedFile)
import Data.Sequence qualified as S
import Data.Word (Word8)
import Debug.Trace
import System.Directory (getCurrentDirectory)
import System.Exit
import System.Posix.Env.ByteString (getArgs)

data Nullary = Nop | Jnz | Add | Sub | MovL | MovR | ShiftL | ShiftR | Dup | Xor | Peek deriving (Enum)

data Instruction = Nullary {getNullary :: Nullary} | Push {getVal :: Integer}

type Stack = [Integer]

data Stacks = Stacks {getCurr :: Stack, getLeft :: [Stack], getRight :: [Stack]}

byteToInstructions :: Word8 -> [Instruction]
byteToInstructions x
  | x `testBit` 7 = [Push . fromIntegral $ (x `clearBit` 7)]
  | otherwise = map (Nullary . toEnum . fromIntegral) [x `div` 11, x `mod` 11]

getInstructions :: B.ByteString -> S.Seq Instruction
getInstructions = S.fromList . concatMap byteToInstructions . B.unpack

binaryOp :: (Integer -> Integer -> Integer) -> Stacks -> Stacks
binaryOp f (Stacks (x : y : ys) l r) = Stacks (f y x : ys) l r

runNullary :: Nullary -> Stacks -> Stacks
runNullary Nop s = s
runNullary Add s = binaryOp (+) s
runNullary Sub s = binaryOp (-) s
runNullary Xor s = binaryOp xor s
runNullary Peek (Stacks [] left right) = Stacks [0] left right
runNullary Peek (Stacks curr@[_] left right) = Stacks (1 : curr) left right
runNullary Peek (Stacks curr left right) = Stacks (2 : curr) left right
runNullary MovL (Stacks (x : curr) (new : left) right) = Stacks curr ((x : new) : left) right
runNullary MovR (Stacks (x : curr) left (new : right)) = Stacks curr left ((x : new) : right)
runNullary ShiftL (Stacks curr (new : left) right) = Stacks new left (curr : right)
runNullary ShiftR (Stacks curr left (new : right)) = Stacks new (curr : left) right
runNullary Dup (Stacks (x : curr) left right) = Stacks (x : x : curr) left right

runInstruction :: Instruction -> Stacks -> Stacks
runInstruction (Push x) (Stacks curr left right) = Stacks (x : curr) left right
runInstruction (Nullary instruction) s = runNullary instruction s

runInstructions :: Int -> S.Seq Instruction -> Stacks -> Stacks
runInstructions i instructions stacks
  | i == S.length instructions = stacks
  | otherwise = case S.lookup i instructions of
      Just (Nullary Jnz) ->
        let (Stacks (x : y : curr) left right) = stacks
            jump = runInstructions (fromIntegral x) instructions
         in (if y /= 0 then jump else runNext) $ Stacks curr left right
      Just x -> runNext (runInstruction x stacks)
  where
    runNext = runInstructions (i + 1) instructions

main = do
  args <- getArgs
  let program = B.fromStrict $(embedFile "asm.out")
  let flag = head args
  let initial = map fromIntegral . B.unpack . B.fromStrict $ flag
  let instructions = getInstructions program
  let stacks = runInstructions 0 instructions (Stacks initial (repeat []) (repeat []))
  let ret = getCurr stacks
  case ret of
    [0] ->
      let hash = Builder.toLazyByteString . Builder.byteStringHex . SHA256.hash $ flag
       in putStrLn (if B.take 8 hash == "7652e062" then "Success" else "Failure")
    _ -> putStrLn "Failure"
