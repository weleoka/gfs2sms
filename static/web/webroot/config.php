<?php
/**
 * Config-file for Roo. Change settings here to affect installation.
 *
 */

/**
 * Set the error reporting.
 *
 */
error_reporting(-1);              // Report all type of errors
ini_set('display_errors', 1);     // Display all errors
ini_set('output_buffering', 0);   // Do not buffer outputs, write directly


/**
 * Define paths and Constants.
 *
 */
define('GFS2SMS_VERSION', 'v0.0.2');
define('ROO_INSTALL_PATH', __DIR__ . '/..');
define('ROO_THEME_PATH', ROO_INSTALL_PATH . '/theme/render.php');
define('GFS2SMS_TOOLS', ROO_INSTALL_PATH . '/../../../');
define('GFS2SMS_GRIB_IN', ROO_INSTALL_PATH . '/../../grib_in/');
define('GFS2SMS_GRIB_OUT', ROO_INSTALL_PATH . '/../../grib_out/');

/**
 * Include bootstrapping functions.
 *
 */
include(ROO_INSTALL_PATH . '/src/bootstrap.php');


/**
 * Start the session.
 *
 */
session_name(preg_replace('/[^a-z\d]/i', '', __DIR__));
session_start();


/**
 * Create the roo variable.
 *
 */
$roo = array();


/**
 * Site wide settings.
 */
$roo['lang']         = 'en';
$roo['title_append'] = ' | Ravensgrib';


 /**
 *  Theme related settings.
 */
//$roo['stylesheet'] = 'css/style.css';
$roo['stylesheetsLESS'] = array(
                      'css/base.less',
                      );
$roo['stylesheets'] = array(
                      '../assets/css/normalize.css',
                      );
$roo['favicon']    = 'favicon.ico';


/**
 *  Settings for JavaScript.
 */
$roo['jsForHead'] = array( '../assets/js/less.min.js',
                                    '../assets/js/modernizr.js',
                                    '../assets/js/respond.min.js',
                                   // '../assets/js/picturefill.min.js',
                                  );

/* Grab Google CDN's jQuery. fall back to local if necessary. 1.12.0 is valid Jan 2016.--> 
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script>!window.jQuery && document.write('<script src="../assets/js/jquery-1.12.0.min.js"><\/script>')</script>*/

// $roo['jquery'] = '//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js';
$roo['jsForFoot'] = array(
                                    '../assets/js/jquery-1.12.0.min.js',
                                   // 'js/mos.js',
                                   // 'js/kai.js',
                                    'js/main.js',
                                  ); // To add extra javascript files


/**
 *  Navigation
 */
$roo['menu'] = array(
  // Use for styling the menu
  'class' => 'navbar',

  // Here comes the menu strcture
  'items' => array(
    // This is a menu item
    'home'  => array(
      'text'  =>'Home',
      'url'   =>'index.php',
      'title' => 'RavensGRIB'
    ),

    // This is a menu item
    'test'  => array(
      'text'  =>'Setup',
      'url'   =>'setup.php',
      'title' => 'How to get started',
    ),


    // This is a menu item
    'about' => array(
      'text'  =>'About',
      'url'   =>'about.php',
      'title' => 'About RavensGRIB.'
    ),

    // This is a menu item
    'docs' => array(
      'text'  =>'Docs',
      'url'   =>'documentation.php',
      'title' => 'Documentation recources.'
    ),
  ),

  // This is the callback tracing the current selected menu item base on scriptname
  'callback' => function($url) {
    if(basename($_SERVER['SCRIPT_FILENAME']) == $url) {
      return true;
    }
  }
);


/**
 *  Google analytics.
 */
$roo['google_analytics'] = null; //'UA-22093351-1'; // Set to null to disable google analytics


/**
 *  Header.
 */
$roo['header'] = <<<EOD
<a href='index.php'>
    <li id='sitelogo' data-src="img/ardeidae02.png" class="decoration" alt='ardeidae logo'></li>
    <!-- <img id='sitelogo' src='img/ardeidae02.png' alt='ardeidae'/> -->
</a>
<span class='sitetitle'>RavensGRIB</span>
EOD;

$roo['headerNvp'] = <<<EOD
<a href='mobileMenu.php'>
  <img id='mobileNavButton' src="img/nvpMenu.png"></img>
</a>
EOD;


/**
 *  Footer.
 */
$roo['footer'] = <<<EOD
Copyright &copy 2016 Kai Weeks.
EOD;
