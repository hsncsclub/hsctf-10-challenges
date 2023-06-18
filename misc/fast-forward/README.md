# fast-forward

Everyone always says Python is too slow—so let's speed it up!

```py
E=type('',(),{'__eq__':lambda s,o:o})();x=vars(str)==E;x["count"]=lambda s,o:s
```
