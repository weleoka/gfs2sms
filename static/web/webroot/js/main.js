/*globals SyntaxHighlighter, Image, Modernizr */
/**
 * Place your JS-code here.
 */
$(document).ready(function(){
  'use strict';

  var getEmbed = function (url) {
    var output = '';
    var youtubeUrl = url.match(/watch\?v=([a-zA-Z0-9\-_]+)/);
    var vimeoUrl = url.match(/^http:\/\/(www\.)?vimeo\.com\/(clip\:)?(\d+).*$/);
    if (youtubeUrl) {
      output = '<div class="vid-wrapper"><iframe src="http://www.youtube.com/embed/'
        + youtubeUrl[1]+'?rel=0" frameboarder="0" allowfullscreen></iframe</div>';
      return output;
    }
    if (vimeoUrl) {
      output = '<div class="vid-wrapper"><iframe src="http://player.vimeo.com/video/'
        + vimeoUrl[3] + '" frameboarder="0"></iframe></div>';
      return output;
    }
  };

  /**
  *  Get certain images only for WVP, lazy load.
  * This is not ideal, as its not a progressive enhancement.
  */
  if ( Modernizr.mq('all and (min-width: 36em)') ) {
    var lazy = $('[data-src]');
    var i, source, img, imgClass, imgId, imgAlt;

    for ( i = 0; i < lazy.length; i++ ) {
      source = lazy[i].getAttribute('data-src');
      imgClass = lazy[i].getAttribute('class');
      imgId = lazy[i].getAttribute('id');
      imgAlt = lazy[i].getAttribute('alt');
      // Crete the image
      img = new Image();
      img.src = source;
      img.class = imgClass;
      img.id = imgId;
      img.alt = imgAlt;
      // Insert it inside the link
      lazy[i].insertBefore(img, lazy[i].firstChild);
    }
  }

  // Toggle downloadButton highlighting.
  $('#download').hover(function() {
    $(this).attr('src', 'img/downloadHover.png');
  }, function() {
    $(this).attr('src', 'img/download.png');
  });


/**
 *  jQuery to toggle NVP (Narrow View Port) menu.
 */
  $('#mobileNavButton').on('click', function (e) {
    $('.navbarNvp').toggle();
    e.preventDefault();
  });

  var navbarMode = $('.navbarNvp li').css('display');
  if (navbarMode === 'block') {
    $('.navbarNvp a').on('click', function () {
      $('.navbarNvp').toggle();
    });
  }


  /* embed the video. Should be with in matchMedia JS test for NVP devices (Narrow View Port) */
  /* Need to rewrite for Jquery syntax */
  var vidLinkHref = $('#video').prop('href');
  if (vidLinkHref) {
    var result = getEmbed(vidLinkHref);
    var parent = vidLinkHref.parentNode;
    parent.innerHTML = result + vidLinkHref.parentNode.innerHTML;
    parent.removeChild(vidLinkHref);
  }

});

