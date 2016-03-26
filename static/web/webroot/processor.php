<?php

include(__DIR__.'/config.php');

$roo['title'] = "Welcome";

$roo['header'] .= '<span class="siteslogan">Bringer of GRIBs</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">RavensGRIB</p>';



/* Data processing. */

// Check if the url contains a querystring with a lat and long.
if(isset($_GET["LAT"]) && isset($_GET["LONG"])) 
{
    $lat = $_GET["LAT"];
    $long = $_GET["LONG"];
}

// Check if request-button was pressed, create a new file. Do some checks before actually creating the data.
// ./wgrib -s -d 1 sample.grb | ./wgrib -i -text sample.grb -o outfile1

$arr = [];
$debug = "";
$grib_processor = GFS2SMS_TOOLS . "wgrib/wgrib";
$grib_file = GFS2SMS_GRIB_IN . "20160325_150423_.grb";
$output_file = GFS2SMS_GRIB_OUT. "newdata.grb";
$flags = "-s -d 1"; // -s Simple, -d Data 1.
$flags2 = "-i -text";   // -i Read from stdin (inventory), -text Output text.

if(isset($_GET['getGRIB'])) {

    if(empty($lat)) {
        $res = "Not a valid latitude value.";
    }

    if(empty($long)) {
        $res = "Not a valid longitude value.";
    
    } else {
        //string exec ( string $command [, array &$output [, int &$return_var ]] )
        $command = "sudo -u deppi " 
            . $grib_processor . " -s -d 1 " . $grib_file 
            . " -o /dev/null"
            . " | sudo -u deppi " 
            . $grib_processor . " -i -text " . $grib_file 
            . " -o " . $output_file;
        exec($command, $arr, $return_var); 
    }
}

if($return_var == 0) {
    $res = "Success!";
/*    $handle = fopen($output_file, 'r') or die("Unable to open file!");
    $count = 0;
    while(!feof($handle)) {
        $buffer = fread($handle, 10);
        $debug .= $count++ . ": " . $buffer;
    }
    fclose($handle);*/

    $myfile = fopen($output_file, "r") or die("Unable to open file!");
    // $debug = fread($myfile,filesize($output_file));
    fclose($myfile);

} else {
    $res = "GRIB processing failed.";
    echo $command;
    $debug .= dump($arr);
}

$roo['main'] = <<<EOD

<div class="articleSegment">
    <h2>RavensGRIB dev.</h2>

    <p><output class="info"><?=$res?></output></p>

    Lat: $lat<br>
    Long: $long<br>
    User feedback: $res<br>
    Process return value: $return_var<br>
    Debug info: $debug<br>

    <br><a href="index.php">Return</a><br>

</div>


EOD;

$roo['footer'];

include(ROO_THEME_PATH);