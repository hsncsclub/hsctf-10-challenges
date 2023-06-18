// ==UserScript==
// @name         Password Manager
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  my very own custom password manager! should be extra secure because no one knows the algorithm!
// @match        *://*/*
// @grant        GM_registerMenuCommand
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

let key = GM_getValue("key");
if(!key){
	key = prompt("Master Key:");
	GM_setValue("key", key);
}

function mod(n, m) {
	return ((n % m) + m) % m;
}

function encrypt(s){
	let out = "";
	for(let i = 0; i < s.length; i++){
		let c = s.charCodeAt(i) - 32;
		let k = key.charCodeAt(i % key.length) - 32;
		out += String.fromCharCode(mod(c + k, 127 - 32) + 32);
	}
	return out;
}

function decrypt(s){
	let out = "";
	for(let i = 0; i < s.length; i++){
		let c = s.charCodeAt(i) - 32;
		let k = key.charCodeAt(i % key.length) - 32;
		out += String.fromCharCode(mod(c - k, 127 - 32) + 32);
	}
	return out;
}

function save_password(){
	let password = prompt("Password:");
	GM_setValue("pwd_" + window.location.hostname, encrypt(password));
}

function load_password(){
	let password = decrypt(GM_getValue("pwd_" + window.location.hostname));
	if(!password){
		console.log("No passwords saved for this site");
		return;
	}

	let inputs = document.querySelectorAll("input[type=password]");
	if(inputs.length == 0){
		console.log("No password boxes found");
		return;
	}
	inputs.forEach(input=>{input.value = password;});
}

GM_registerMenuCommand("Save Password", save_password);
GM_registerMenuCommand("Fill Password", load_password);

