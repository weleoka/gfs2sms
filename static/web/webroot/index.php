<?php

include(__DIR__.'/config.php');

$roo['title'] = "Welcome";

$roo['header'] .= '<span class="siteslogan">Bringer of GRIBs</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">RavensGRIB</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB dev.</h2>

<form method="GET" action="processor.php">
	<h3>Request Form</h3>
	<div>
		<input type="text" placeholder="" value="22" required="" name="LAT" />
	</div>
	<div>
		<input type="text" placeholder="" value="33" required="" name="LONG" />
	</div>
	<div>
		<input type="submit" value="Request GRIB" name="getGRIB" /><br>
		<input type="reset" value="Reset"><br>
		<a href="#">Need help?</a><br>
		<a href="#">Register</a>
	</div>
</form><!-- form -->
	
	<div class="button">
		<a href="#">Download source file</a>
	</div><!-- button -->

<p></p>
<p></p>
<p></p>
<p></p>
</div>


EOD;

$roo['footer'];

include(ROO_THEME_PATH);