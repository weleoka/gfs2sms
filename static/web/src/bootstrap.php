<?php
/**
 * Bootstrapping functions, essential and needed for Roo to work together with some common helpers.
 *
 */

/**
 * Default exception handler.
 *
 */
function myExceptionHandler($exception) {
  echo "Roo: Uncaught exception: <p>" . $exception->getLine() . " - " . $exception->getMessage() . "</p><pre>" . $exception->getTraceAsString(), "</pre>";
}
set_exception_handler('myExceptionHandler'); // Makes the function into a class which extends Exception.


/**
 * Autoloader for classes.
 *
 */
/*
function myAutoloader($class) {
  $path = ROO_INSTALL_PATH . "/src/{$class}/{$class}.php";
  if(is_file($path)) {
    include($path);
  }
  else {
    throw new Exception("Classfile '{$class}' does not exists.");
  }
}
spl_autoload_register('myAutoloader');
*/


/**
 * Including composer autoloader if available.
 *
 * @link https://getcomposer.org/doc/01-basic-usage.md#autoloading
 */
if(is_file(ROO_INSTALL_PATH . '/vendor/autoload.php')) {
    include ROO_INSTALL_PATH . '/vendor/autoload.php';
}



/**
 * Dump-function.
 *
 */
function dump($array) {
  echo "<pre>" . htmlentities(print_r($array, 1)) . "</pre>";
}
// anropa funktionen så här: dump($_SERVER);