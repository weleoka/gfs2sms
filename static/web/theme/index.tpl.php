<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html lang='<?=$lang?>' class='no-js'> <!--<![endif]-->
<!-- Modernizr will replace the class 'no-js' with a list of features supported by the browser.
But you need to read about the IE specific classnames above... Seen used in conjunction with
(modernizr-2.8.3-respond-1.4.2.min.js). Also read about browserconfig.xml in webroot. -->

<head>
	<meta charset='utf-8'/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        	<meta name="description" content="">

        	<link rel="apple-touch-icon" href="apple-touch-icon.png">

	<!-- Set the viewport, notice its in non-accessibility mode at the moment -->
	<meta name='viewport' content='width=device-width, initial-scale=1.0, minimum-scale=1.0, user-scalable=no' />
	<!-- dont let scroll vertical <meta name='viewport' content='height=device-height' /> -->

	<!-- iOS specifics -->
	<!-- Beware the iOS orientation bug <meta name='viewport' content='user-scalable=no' /> -->
	<!-- Link to app on iTunes <meta name="apple-itunes-app" content="app-id=XXXXXXXXX"> -->
	<!-- Launch as app, without browser chrome from iOS homescreen <meta name="apple-mobile-web-app-capable" content="yes"/> -->
	<!---->

	<title><?=get_title($title)?></title>

	<?php if(isset($favicon)): ?>
		<link rel='shortcut icon' href='<?=$favicon?>' />
	<?php endif; ?>

	<?php foreach($stylesheets as $val): ?>
		<link rel='stylesheet' type='text/css' href='<?=$val?>' />
	<?php endforeach; ?>

	<?php foreach($stylesheetsLESS as $val): ?>
		<link rel='stylesheet/less' type='text/css' href='<?=$val?>' />
	<?php endforeach; ?>

	<?php if(isset($jsForHead)): foreach($jsForHead as $val): ?>
		<script src='<?=$val?>'></script>
	<?php endforeach; endif; ?>

	<!-- LESS CSS client side compiler set development mode -->
	<script type="text/javascript">less = { env: 'development' };</script>

	<!-- HTML5 Shiv current 03.03.2015 -->
	<!--[if lt IE 9]>
		<script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.min.js"></script>
	<![endif]-->

</head>

<body>
	<div id='wrapper'>
   	<div id='header'><?=$header?><pre id='versionNum'>February 2016<br><?=GFS2SMS_VERSION?></pre></div>
   	<div id='headerNvp'><?=$headerNvp?></div>

 	<?php if(isset($menu)): ?>
	 	<div id='navbar'>
	 		<?=get_navbar2($menu)?>
	 	</div>

	 	<div id='navbarNvpWrapper'>
	 		<?php $menuNvp = $menu; $menuNvp['class'] = 'navbarNvp'; ?>
	 		<?=get_navbar2($menuNvp)?>
	 	</div>
	<?php endif; ?>

   	<div id='main' class='box-shadow'><h4>First seen 2015!</h4><?=$main?></div>
   	<div id='footer'><?=$footer?></div>
	</div>

	<?php if(isset($jsForFoot)): foreach($jsForFoot as $val): ?>
		<script src='<?=$val?>'></script>
	<?php endforeach; endif; ?>

	<?php if(isset($google_analytics)): ?>
		<script>
 		 var _gaq=[['_setAccount','<?=$google_analytics?>'],['_trackPageview']];
 		 (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
 		 g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
 		 s.parentNode.insertBefore(g,s)}(document,'script'));
		</script>
	<?php endif; ?>

</body>
</html>