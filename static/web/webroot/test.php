<?php


// Libsodium PECL test
echo "\nlibsodium major and minor version: ";
var_dump([
    \Sodium\library_version_major(),
    \Sodium\library_version_minor(),
    \Sodium\version_string()
]);
echo "\ncurrent version of the sodium library: ";
var_dump([\Sodium\version_string()]);


// Libsodium password hashing tests:
// https://download.libsodium.org/doc/password_hashing/index.html
// https://paragonie.com/book/pecl-libsodium/read/07-password-hashing.md
echo "\nCurrent hash keybytes: "
		. \Sodium\CRYPTO_GENERICHASH_KEYBYTES;
echo "\nCurrent salt keybytes: "
		. \Sodium\CRYPTO_PWHASH_SCRYPTSALSA208SHA256_SALTBYTES;
echo "\nOPSLIMIT: "
		. \Sodium\CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_INTERACTIVE;
echo "\nMEMLIMIT (bytes): "
		. \Sodium\CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_INTERACTIVE;


// Predis. A PHP binding for Redis database.
echo"\n";