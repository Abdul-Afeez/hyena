from app.tools.parser import Parser

parser = Parser({
   "url":"https://techcabal.com/",
   "h1":[
      [
         "h1",
         "class",
         "single-article-title",
         "0"
      ],
      "text"
   ],
   "date":[
      [
         "span",
         "class",
         "single-article-date",
         "0"
      ],
      "text"
   ],
   "date_engine":[
      "_january_01_1970"
   ],
   "description":[
      [
         "meta",
         "property",
         "og:description",
         "0"
      ],
      "content"
   ],
   "main_content":[
      [
         "main",
         "",
         "",
         1
      ],
      "contents"
   ],
   "terminator":"Share this article",
   "unwanted_blocks":[
      [
         [
            "div",
            "class",
            "single-article-category",
            "0"
         ],
         "tag",
         True
      ],
      [
         [
            "div",
            "class",
            "list-newsletter-form shortcode",
            "0"
         ],
         "tag",
         True
      ]
   ],
"bad_signatures": [[["div", "class", "single-article-category", "0"], "text", "newsletters"]],"image_source": "TechCabal"
})
data = parser.extract('', '''

<!doctype html>
<html lang="en-US" class="no-js">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="pingback" href="https://techcabal.com/xmlrpc.php">
    
    <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO plugin v19.6.1 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>22 things that happened for the first time in 2022 in the African tech scene | TechCabal</title>
	<meta name="description" content="Here’s a list of 22 things that happened for the first time in the African tech scene in 2022" />
	<link rel="canonical" href="http://techcabal.com/2022/12/30/22-things-first-time-in-2022-in-the-african-tech-scene/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="22 things that happened for the first time in 2022 in the African tech scene | TechCabal" />
	<meta property="og:description" content="Here’s a list of 22 things that happened for the first time in the African tech scene in 2022" />
	<meta property="og:url" content="http://techcabal.com/2022/12/30/22-things-first-time-in-2022-in-the-african-tech-scene/" />
	<meta property="og:site_name" content="TechCabal" />
	<meta property="article:publisher" content="https://www.facebook.com/TechCabal" />
	<meta property="article:published_time" content="2022-12-30T10:00:00+00:00" />
	<meta property="article:modified_time" content="2022-12-27T22:48:58+00:00" />
	<meta property="og:image" content="http://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech-.png" />
	<meta property="og:image:width" content="2100" />
	<meta property="og:image:height" content="1100" />
	<meta property="og:image:type" content="image/png" />
	<meta name="author" content="Daniel Adeyemi" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@Danieltadeyemi" />
	<meta name="twitter:site" content="@techcabal" />
	<meta name="twitter:label1" content="Written by" />
	<meta name="twitter:data1" content="Daniel Adeyemi" />
	<meta name="twitter:label2" content="Est. reading time" />
	<meta name="twitter:data2" content="13 minutes" />
	<!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Feed" href="https://techcabal.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Comments Feed" href="https://techcabal.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; 22 things that happened for the first time in 2022 in the African tech scene Comments Feed" href="https://techcabal.com/2022/12/30/22-things-first-time-in-2022-in-the-african-tech-scene/feed/" />
<script type="text/javascript">
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/x7d4c5z5.stackpathcdn.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.0.2"}};
/*! This file is auto-generated */
!function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){var a=String.fromCharCode,e=(p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,e),0,0),i.toDataURL());return p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,t),0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(!p||!p.fillText)return!1;switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])?!1:!s([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!s([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]);case"emoji":return!s([129777,127995,8205,129778,127999],[129777,127995,8203,129778,127999])}return!1}(o[r]),t.supports.everything=t.supports.everything&&t.supports[o[r]],"flag"!==o[r]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[o[r]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(e=t.source||{}).concatemoji?c(e.concatemoji):e.wpemoji&&e.twemoji&&(c(e.twemoji),c(e.wpemoji)))}(window,document,window._wpemojiSettings);
</script>
<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 0.07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<link rel='stylesheet' id='wp-block-library-css'  href='https://x7d4c5z5.stackpathcdn.com/wp-includes/css/dist/block-library/style.min.css?ver=6.0.2' type='text/css' media='all' />
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
</style>
<link rel='stylesheet' id='wordpress-popular-posts-css-css'  href='//x7d4c5z5.stackpathcdn.com/wp-content/plugins/wordpress-popular-posts/assets/css/wpp.css?ver=6.0.5' type='text/css' media='all' />
<link rel='stylesheet' id='parent-style-css'  href='//x7d4c5z5.stackpathcdn.com/wp-content/themes/bcm/style.css?ver=7.0.1' type='text/css' media='all' />
<link rel='stylesheet' id='child-style-css'  href='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/style.css?ver=7.0.1' type='text/css' media='all' />
<script type='application/json' id='wpp-json'>
{"sampling_active":0,"sampling_rate":100,"ajax_url":"https:\/\/techcabal.com\/wp-json\/wordpress-popular-posts\/v1\/popular-posts","api_url":"https:\/\/techcabal.com\/wp-json\/wordpress-popular-posts","ID":105193,"token":"ace5a9af60","lang":0,"debug":0}
</script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/plugins/wordpress-popular-posts/assets/js/wpp.min.js?ver=6.0.5' id='wpp-js-js'></script>
<link rel="https://api.w.org/" href="https://techcabal.com/wp-json/" /><link rel="alternate" type="application/json" href="https://techcabal.com/wp-json/wp/v2/posts/105193" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://techcabal.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://techcabal.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 6.0.2" />
<link rel='shortlink' href='https://techcabal.com/?p=105193' />
<link rel="alternate" type="application/json+oembed" href="https://techcabal.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://techcabal.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F&#038;format=xml" />
            <style id="wpp-loading-animation-styles">@-webkit-keyframes bgslide{from{background-position-x:0}to{background-position-x:-200%}}@keyframes bgslide{from{background-position-x:0}to{background-position-x:-200%}}.wpp-widget-placeholder,.wpp-widget-block-placeholder{margin:0 auto;width:60px;height:3px;background:#dd3737;background:linear-gradient(90deg,#dd3737 0%,#571313 10%,#dd3737 100%);background-size:200% auto;border-radius:3px;-webkit-animation:bgslide 1s infinite linear;animation:bgslide 1s infinite linear}</style>
            <link rel="manifest" href="/wp-content/themes/tc2.0/manifest.webmanifest"><meta name="theme-color" content="#F23204">      <meta name="onesignal" content="wordpress-plugin"/>
            <script>

      window.OneSignal = window.OneSignal || [];

      OneSignal.push( function() {
        OneSignal.SERVICE_WORKER_UPDATER_PATH = "OneSignalSDKUpdaterWorker.js.php";
                      OneSignal.SERVICE_WORKER_PATH = "OneSignalSDKWorker.js.php";
                      OneSignal.SERVICE_WORKER_PARAM = { scope: "/" };
        OneSignal.setDefaultNotificationUrl("https://techcabal.com");
        var oneSignal_options = {};
        window._oneSignalInitOptions = oneSignal_options;

        oneSignal_options['wordpress'] = true;
oneSignal_options['appId'] = '8cecd005-d1a8-4962-a44e-5b304f7eef03';
oneSignal_options['allowLocalhostAsSecureOrigin'] = true;
oneSignal_options['welcomeNotification'] = { };
oneSignal_options['welcomeNotification']['title'] = "TechCabal";
oneSignal_options['welcomeNotification']['message'] = "";
oneSignal_options['path'] = "/wp-content/plugins/onesignal-free-web-push-notifications/sdk_files/";
oneSignal_options['safari_web_id'] = "web.onesignal.auto.2d9123a5-f6c1-46fe-a6d4-d9acca55dc3d";
oneSignal_options['promptOptions'] = { };
oneSignal_options['promptOptions']['actionMessage'] = "Want to stay up to date on tech and innovation in Africa?";
oneSignal_options['promptOptions']['acceptButtonText'] = "Yes please";
oneSignal_options['promptOptions']['cancelButtonText'] = "No";
oneSignal_options['promptOptions']['siteName'] = "http://techcabal.com/";
oneSignal_options['notifyButton'] = { };
oneSignal_options['notifyButton']['enable'] = true;
oneSignal_options['notifyButton']['position'] = 'bottom-right';
oneSignal_options['notifyButton']['theme'] = 'default';
oneSignal_options['notifyButton']['size'] = 'medium';
oneSignal_options['notifyButton']['showCredit'] = true;
oneSignal_options['notifyButton']['text'] = {};
                OneSignal.init(window._oneSignalInitOptions);
                OneSignal.showSlidedownPrompt();      });

      function documentInitOneSignal() {
        var oneSignal_elements = document.getElementsByClassName("OneSignal-prompt");

        var oneSignalLinkClickHandler = function(event) { OneSignal.push(['registerForPushNotifications']); event.preventDefault(); };        for(var i = 0; i < oneSignal_elements.length; i++)
          oneSignal_elements[i].addEventListener('click', oneSignalLinkClickHandler, false);
      }

      if (document.readyState === 'complete') {
           documentInitOneSignal();
      }
      else {
           window.addEventListener("load", function(event){
               documentInitOneSignal();
          });
      }
    </script>
<link rel="icon" href="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2018/10/cropped-tcbig-32x32.png" sizes="32x32" />
<link rel="icon" href="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2018/10/cropped-tcbig-192x192.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2018/10/cropped-tcbig-180x180.png" />
<meta name="msapplication-TileImage" content="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2018/10/cropped-tcbig-270x270.png" />
		<style type="text/css" id="wp-custom-css">
			.postid-91540 .comment-section,
.postid-91742 .comment-section {
	display: none;
}

.dark .single-report-content .single-report-title {
	color: #fff;
}		</style>
		<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Courier+Prime:400,700&display=swap" rel="stylesheet" async>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-39740518-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
                    gtag('set', {
                'author' : "Daniel Adeyemi",
                'pagetitle' : "22 things that happened for the first time in 2022 in the African tech scene",
                'publishdate' : "2022-12-30"
            });
                gtag('config', 'UA-39740518-1', {
            custom_map: {
                'dimension1' : 'author',
                'dimension2' : 'pagetitle',
                'dimension3' : 'publishdate'
                // 'dimension4' : 'online'
            }
        });
            </script>
    <!-- Microsoft Clarity -->
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){
            c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", 'dj4irs9dxc');
    </script>
    <!-- End Microsoft Clarity -->
    	<!-- Twitter conversion tracking base code -->
	<script>
	    !function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
	    },s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='https://static.ads-twitter.com/uwt.js',
	        a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
	    twq('config','o4s13');
	</script>
    <!-- End Twitter conversion tracking base code -->
	<!-- MailerLite Universal -->
<script>
    (function(m,a,i,l,e,r){ m['MailerLiteObject']=e;function f(){
        var c={ a:arguments,q:[]};var r=this.push(c);return "number"!=typeof r?r:f.bind(c.q);}
        f.q=f.q||[];m[e]=m[e]||f.bind(f.q);m[e].q=m[e].q||f.q;r=a.createElement(i);
        var _=a.getElementsByTagName(i)[0];r.async=1;r.src=l+'?v'+(~~(new Date().getTime()/1000000));
        _.parentNode.insertBefore(r,_);})(window, document, 'script', 'https://static.mailerlite.com/js/universal.js', 'ml');

    var ml_account = ml('accounts', '3145054', 'i5e6q9e2j9', 'load');
</script>
<!-- End MailerLite Universal --><script async src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script><meta name="facebook-domain-verification" content="ilurlom1mtlm8x0xxa05pllyoyypln" /></head>

<body class="post-template-default single single-post postid-105193 single-format-standard  section-single"><div id="fb-root"></div>
<script>
    (function(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id)) return;
		js = d.createElement(s); js.id = id;
		js.src = 'https://connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v3.1&appId=252296078952383&autoLogAppEvents=1';
		fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));
</script>

<!-- Facebook Pixel Code -->
<script>
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
        n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window, document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '2323713477867801');
    fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=2323713477867801&ev=PageView&noscript=1"/></noscript>
<!-- End Facebook Pixel Code --><div class="mobile">
    <div class="smart-banner" style="display:none;">
        <a class="smart-banner-link" href="/"><img style="display: block;" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-smart-banner.jpg" width="100%" height="auto" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-smart-banner.jpg 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-smart-banner@2x.jpg 2x" alt="TechCabal Smart Banner"></a>
    </div>
</div>
<div class="top-ad" id="top-ad">
    <div class="ad-box"><div class="ad" id="div-db-0"></div></div></div>
<div id="wrapper">
    <header class="header" id="header">
        <div class="content">
            <div class="logo">
                <a href="/"><img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop.png" width="182" height="39" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop@2x.png 2x" alt="TechCabal"></a>
            </div>

            <!-- Quick Links -->
            <!-- Move to base function and adapt to wp query -->
<div id="quick-links">
    <span>Quick Links</span>
    <div class="menu-wrapper"><ul class="menu"><li><a href="https://techcabal.com/tag/acquisition/">acquisition</a></li><li><a href="https://techcabal.com/tag/africa/">Africa</a></li><li><a href="https://techcabal.com/tag/african-startups/">African startups</a></li><li><a href="https://techcabal.com/tag/african-tech-roundup/">African tech roundup</a></li><li><a href="https://techcabal.com/tag/francophone-africa/">francophone africa</a></li><li><a href="https://techcabal.com/tag/kenya/">Kenya</a></li><li><a href="https://techcabal.com/tag/mtn/">MTN</a></li><li><a href="https://techcabal.com/tag/nairobi/">Nairobi</a></li><li><a href="https://techcabal.com/tag/nigeria/">Nigeria</a></li><li><a href="https://techcabal.com/tag/south-africa/">South Africa</a></li><li><a href="https://techcabal.com/tag/vodacom/">Vodacom</a></li></ul></div></div>
            <ul class="icon-menu">
                <li class="icon-menu-item">
                    <span id="switch-mode-trigger" class="switch-mode-trigger">
                        <input type="checkbox" style="display: none;" id="switch-mode">
                        <span class="icon-menu-img"></span>
                        <span class="icon-menu-text">Dark/Light</span>
                    </span>
                </li>
                <li class="icon-menu-item">
                    <a href="/search" class="search-open">
                        <span class="icon-menu-img"></span>
                        <span class="icon-menu-text">Search</span>
                    </a>
                </li>
                <li class="icon-menu-item">
                    <span class="menu-open">
                        <span class="icon-menu-img"></span>
                        <span class="icon-menu-text">Menu</span>
                    </span>
                </li>
            </ul>
        </div>

        <!-- Mega Menu -->
        <div id="mega-menu" class="mega-menu">
    <div class="content">
        <div class="search-social">
            <div class="logo">
                <a href="/">
                    <span class="desktop"><img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop.png" width="210" height="45" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop@2x.png 2x" alt="TechCabal"></span>
                    <span class="mobile"><img loading="lazy"  src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-logo-mobile-top.png" width="72" height="72" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-logo-mobile-top.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-logo-mobile-top@2x.png 2x" alt="TechCabal"></span>
                </a>
            </div>
            <div class="search-box">
                <span>Search</span>
                <form method="GET" action="/" class="search">
                    <input type="search" id="search-box" name="s" placeholder="Search" required value="">
                    <button class="search-button">
                        <img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-search-colored.png" width="20" height="20" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-search-colored.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-search-colored@2x.png 2x" alt="Menu">
                    </button>
                </form>
            </div>
            <div class="social-widget social-follow">
                <span>Follow us</span>
                <ul class="social-links">
    <li><a href="https://twitter.com/TechCabal" target="_blank" class="social-icon social-twitter"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png" alt="Twitter" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red@2x.png 2x"></a></li><li><a href="https://www.linkedin.com/company/techcabal/" target="_blank" class="social-icon social-linkedin"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png" alt="Linkedin" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red@2x.png 2x"></a></li><li><a href="https://www.facebook.com/TechCabal/" target="_blank" class="social-icon social-facebook"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png" alt="Facebook" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red@2x.png 2x"></a></li><li><a href="https://www.instagram.com/techcabal/" target="_blank" class="social-icon social-instagram"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/instagram_red.png" alt="Instagram" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/instagram_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/instagram_red@2x.png 2x"></a></li><li><a href="https://www.youtube.com/user/TechCabal" target="_blank" class="social-icon social-youtube"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/youtube_red.png" alt="Youtube" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/youtube_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/youtube_red@2x.png 2x"></a></li></ul>            </div>
        </div>
        <div class="main-menu">
            <div class="main-menu-top">
                <ul id="menu-navigation" class="menu"><li id="menu-item-78430" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-78430"><a href="https://techcabal.com/categories">Flagships</a>
<ul class="sub-menu">
	<li id="menu-item-78371" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78371"><a href="https://techcabal.com/category/ask-an-investor/">Ask An Investor</a></li>
	<li id="menu-item-78431" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78431"><a href="https://techcabal.com/category/centre-stage/">Centre Stage</a></li>
	<li id="menu-item-78278" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78278"><a href="https://techcabal.com/category/my-life-in-tech/">My Life In Tech</a></li>
	<li id="menu-item-78279" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78279"><a href="https://techcabal.com/category/factsheet/">Factsheet</a></li>
	<li id="menu-item-78280" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78280"><a href="https://techcabal.com/category/digital-nomads-africa/">Digital Nomads</a></li>
	<li id="menu-item-78281" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78281"><a href="https://techcabal.com/category/the-backend/">The BackEnd</a></li>
	<li id="menu-item-89034" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-89034"><a href="https://techcabal.com/category/web3/">Web3</a></li>
	<li id="menu-item-89035" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-89035"><a href="https://techcabal.com/category/quick-fire/">Quick Fire</a></li>
</ul>
</li>
<li id="menu-item-78282" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-78282"><a href="https://techcabal.com/category/newsletters/">Newsletters</a>
<ul class="sub-menu">
	<li id="menu-item-57883" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-57883"><a href="https://techcabal.com/category/newsletters/tc-daily/">TC Daily</a></li>
	<li id="menu-item-99139" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-99139"><a href="https://techcabal.com/category/newsletters/entering-tech/">Entering Tech</a></li>
	<li id="menu-item-78283" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78283"><a href="https://techcabal.com/category/newsletters/next-wave/">The Next Wave</a></li>
	<li id="menu-item-93569" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-93569"><a href="https://techcabal.com/category/newsletters/tc-weekender/">TC Weekender</a></li>
</ul>
</li>
<li id="menu-item-62014" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-62014"><a href="https://techcabal.com/events">Events</a></li>
<li id="menu-item-78284" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-78284"><a href="https://techcabal.com/reports">Reports</a></li>
<li id="menu-item-78288" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-78288"><a href="https://techcabal.com/tcinsights/">TC Insights</a></li>
<li id="menu-item-78287" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-78287"><a href="https://techcabal.com/category/video/">Video</a></li>
<li id="menu-item-89834" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-89834"><a href="https://techcabal.com/shop/">Shop</a></li>
</ul>            </div>
            <div class="main-menu-bottom">
                <ul id="menu-main-menu-bottom" class="menu"><li id="menu-item-78290" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-78290"><a href="https://techcabal.com/about/">About</a></li>
<li id="menu-item-57891" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-57891"><a href="https://techcabal.com/advertise/">Advertise</a></li>
<li id="menu-item-78291" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-78291"><a href="http://techwomenlagos.com">Tech Women Lagos</a></li>
</ul>            </div>
        </div>
        <div class="mega-menu-ad">
            <div class="ad-box"><div class="ad" id="div-db-1"></div></div>        </div>
        <span id="menu-close" class="menu-close"></span>
    </div>
</div>        <script async>
            let mode_switcher=document.getElementById("switch-mode"),mode_trigger=document.getElementById("switch-mode-trigger"),doc_body=document.querySelector("body");window.localStorage.getItem("dark_mode")&&doc_body.classList.add("dark"),mode_trigger.addEventListener("click",function(){mode_switcher.click()}),mode_switcher.addEventListener("change",function(){this.checked?(doc_body.classList.add("dark"),window.localStorage.setItem("dark_mode",!0)):(doc_body.classList.remove("dark"),window.localStorage.removeItem("dark_mode"))}),window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches&&null===window.localStorage.getItem("dark_mode")&&doc_body.classList.add("dark");
        </script>
    </header>
    <div class="floating-menu mobile" id="floating-menu">
        <ul>
            <li class="floating-menu-item">
                <span class="menu-open">
                    <img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-menu-white.png" width="auto" height="18" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-menu-white.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-menu-white@2x.png 2x" alt="Menu">
                    <span class="icon-menu-text">Menu</span>
                </span>
            </li>
            <li class="floating-menu-item">
                <a href="/categories">
                    <img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-categories.png" width="auto" height="18" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-categories.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-categories@2x.png 2x" alt="Categories">
                    <span class="icon-menu-text">Categories</span>
                </a>
            </li>
            <li class="floating-menu-item">
                <a href="/newsletter">
                    <img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-envelope.png" width="auto" height="18" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-envelope.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-envelope@2x.png 2x" alt="Newsletter">
                    <span class="icon-menu-text">Newsletter</span>
                </a>
            </li>
            <li class="floating-menu-item">
                <a href="/events">
                    <img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-calendar.png" width="auto" height="18" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-calendar.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc2-calendar@2x.png 2x" alt="Calendar">
                    <span class="icon-menu-text">Events</span>
                </a>
            </li>
        </ul>
    </div>
    <div class="main-content">
        <main>
<script type='application/ld+json'>{"@context":"https:\/\/schema.org\/","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/techcabal.com\/2022\/12\/30\/22-things-first-time-in-2022-in-the-african-tech-scene\/"},"headline":"22 things that happened for the first time in 2022 in the African tech scene","image":["https:\/\/x7d4c5z5.stackpathcdn.com\/wp-content\/uploads\/tc\/2022\/12\/Africa-tech-.png"],"datePublished":"2022-12-30T11:00:00+01:00","dateModified":"2022-12-27T23:48:58+01:00","author":{"@type":"Person","name":"Daniel Adeyemi"},"publisher":{"@type":"Organization","url":"https:\/\/techcabal.com","name":"TechCabal","logo":"https:\/\/x7d4c5z5.stackpathcdn.com\/wp-content\/themes\/tc1.5\/images\/tclogo-desktop.png"}}</script><section class="single-article">
    <div class="content">
        <article>
            <div class="single-article-meta">
                <div class="single-article-category">
                    <a href="https://techcabal.com/category/african-tech-roundup/">African Tech Roundup</a>
                </div>
                <h1 class="single-article-title">22 things that happened for the first time in 2022 in the African tech scene</h1>
                <div class="single-article-info">
                    <span class="single-article-author">By
                                                        <a href="https://techcabal.com/author/daniel/" title="Posts by Daniel Adeyemi" rel="author">Daniel Adeyemi</a>                                                </span>
                    <span class="single-article-date">Dec 30, 2022</span>
                </div>
                                        <div class="single-article-img poster-image">
                            <div class="image-holder"><img width="2100" height="1100" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech-.png" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech-.png 2100w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--300x157.jpg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--1024x536.jpg 1024w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--768x402.jpg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--1536x805.jpg 1536w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--2048x1073.jpg 2048w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--690x361.jpg 690w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Africa-tech--1050x550.jpg 1050w" sizes="(max-width: 2100px) 100vw, 2100px" /></div>
                                                                <p class="wp-caption-text">
                                        Source: Africa Business 2020                                    </p>
                                                        </div>
                                </div>
            <div class="single-article-main">
                <div class="single-article-content" id="single-article">
                   
<p>2022 was a different year for the African tech ecosystem as the effects of the economic downturn shook the ecosystem. The year was filled with stories of triumph, failures, and progress. Here’s a list of 22 things that happened for the first time in the African tech ecosystem this year.&nbsp;</p>



<ol><li><strong>Kenya became the first African country to teach coding as a subject in schools</strong></li></ol>



<p>In August, former Kenyan president, Uhuru Kenyatta, <a href="https://techcabal.com/2022/08/08/kenya-becomes-the-first-african-country-to-teach-coding-as-subject-in-schools/" target="_blank" rel="noreferrer noopener">announced</a> the addition of computer programming as a subject in its primary and secondary schools curricula. This announcement was well received because computer programming teaches children to experiment and gives them the confidence to be creative. It’s also seen as a move to ensure that Kenya continues to maintain its place as one of the hotbeds for digital innovation on the continent. </p>



<p>The South African Department of Education made a similar <a href="https://techcabal.com/2022/09/02/south-africa-establishes-artificial-intelligence-institute/" target="_blank" rel="noreferrer noopener">announcement</a> earlier in the year about introducing coding and robotics to schools.</p>



<ol start="2"><li><strong>Nigeria and DRC Congo now have startup acts</strong></li></ol>



<p>Across Africa regulation is seen as an essential tool required to foster innovation. This has led to a clamour for supporting regulation for the tech ecosystem through startup acts. A startup act is a legal and institutional framework for the advancement of startups in a country. It helps to create an environment that encourages the formation, growth, and operation of startups within a country.</p>



<p>In December 2019, Senegal became the second African nation to enact a national startup act, following Tunisia’s landmark bill that passed in April 2018.  This year <a href="https://techcabal.com/2022/10/19/the-nigeria-startup-bill-has-been-approved/" target="_blank" rel="noreferrer noopener">Nigeria</a> and <a href="https://techcabal.com/2022/12/02/the-democratic-republic-of-congo-business-with-startup-act/" target="_blank" rel="noreferrer noopener">DRC</a> joined that list of African countries that have startup acts.</p>



<p>Over 10 African countries, including <a href="https://techweez.com/2021/12/03/startup-bill-2021-passed-kenya-senate/" target="_blank" rel="noreferrer noopener">Kenya</a>, Rwanda, Ghana, and <a href="https://www.thereporterethiopia.com/26274/" target="_blank" rel="noreferrer noopener">Ethiopia</a>, are still in the process of drafting their startup bills.  </p>



<ol start="3"><li><strong>The Central African Republic became the first African country to make bitcoin legal tender</strong></li></ol>



<p>Bitcoin has gained worldwide popularity and use in the past decade—with global adoption growing by <a href="https://blog.chainalysis.com/reports/2021-global-crypto-adoption-index/" target="_blank" rel="noreferrer noopener">2,300%</a> since 2019 and <a href="https://www.investopedia.com/articles/forex/041515/countries-where-bitcoin-legal-illegal.asp" target="_blank" rel="noreferrer noopener">103 countries allowing crypto trading</a>. (Governments and regulators worldwide are still debating its safety.) </p>



<p>In April, the Central African Republic (CAR) <a href="https://techcabal.com/2022/04/27/car-the-first-african-country-to-adopt-bitcoin/" target="_blank" rel="noreferrer noopener">became</a> the first African country to make bitcoin legal tender, and the second country in the world after El Salvador. This means that bitcoin must be accepted as payment alongside the Central African CFA franc.</p>



<p>Closely related to this,<strong> </strong>South Africa’s Financial Sector Conduct Authority (FSCA), through the Financial Advisory and Intermediary Services (FAIS) Act, in October <a href="https://techcabal.com/2022/10/21/crypto-assets-now-financial-products-in-south-africa/" target="_blank" rel="noreferrer noopener">declared</a> that cryptocurrency assets are classified as financial products, allowing them to be regulated.</p>



<p>These two African countries are outliers, compared to many African countries that have banned crypto or restricted its use. Four African countries—Algeria, Egypt, Morocco, and Tunisia—have banned all forms of crypto trading, while seven including Nigeria, Cameroon, and Gabon, have some forms of prohibition regarding crypto trading. These governments have cited numerous reasons for the bans, from fraud and money laundering to tax evasion and terrorist financing.&nbsp;</p>



<ol start="4"><li><strong>A massive wave of layoffs</strong></li></ol>



<p>Layoffs are a common occurrence during an economic downturn and African startup employees weren’t exempt from experiencing them this year. </p>



<p>Data from layoffs.fyi, a crowdsourced database of tech layoffs, shows that 1,495 tech companies have sacked 246,267 employees since the onset of COVID-19. Over 50,000 of such layoffs happened in 2022, with at least over 1,000 tech workers in Africa laid off.&nbsp;</p>



<p>The layoffs started with Egyptian mobility startup Swvl laying off about <a href="https://techcabal.com/2022/05/31/egypt-swvl-lays-off-a-third-of-its-staff-two-months-after-going-public/" target="_blank" rel="noreferrer noopener">400 people</a> in May. Startups such as <a href="https://techcrunch.com/2022/11/16/kenyas-twiga-dismisses-in-house-sales-team-affecting-21-of-it-employees/" target="_blank" rel="noreferrer noopener">Twiga foods</a>, <a href="https://techcabal.com/2022/11/24/nigerian-crypto-exchange-quidax-lays-off-20-of-its-workforce/" target="_blank" rel="noreferrer noopener">Quidax</a>, <a href="https://techcabal.com/2022/11/25/nigerian-food-procurement-platform-vendease-lays-off-9-of-its-workforce/" target="_blank" rel="noreferrer noopener">Vendease</a>, <a href="https://techcabal.com/2022/10/25/54gene-ceo-step-down/" target="_blank" rel="noreferrer noopener">54 Gene</a>, <a href="https://techcabal.com/2022/11/09/after-laying-off-30-of-its-workforce-sendy-receives-funding-from-japanese-vc-mol-plus/" target="_blank" rel="noreferrer noopener">Sendy</a> and many more also carried out a similar exercise, attributing it to the economic downturn.</p>



<ol start="5"><li><strong>Nigerian fintech companies battled with fraud allegations in Kenya</strong></li></ol>



<p>Nigerian startups were under scrutiny by Kenyan Government agencies, particularly the Central Bank of Kenya and its Asset Recovery Agency (ARA), over allegations of card fraud and international money laundering.</p>



<p>Flutterwave Payment Technology Limited, Boxtrip Travel and Tours Limited, Bagtrip Travel Limited, Elivalat Fintech Limited, Adguru Technology Limited, Hupesi Solutions, Cruz Ride Auto Limited, Korapay, and one Simon Ngige were all accused of money laundering.&nbsp;</p>



<p>A number of these fintech companies such as Flutterwave, <a href="https://techcabal.com/2022/11/23/korapay-cleared-of-allegations/" target="_blank" rel="noreferrer noopener">Kora Pay and Kandon</a> have been cleared of these fraud charges.</p>



<ol start="6"><li><strong>Over $4 billion raised in venture capital funding</strong></li></ol>



<p>The jury is still out on how much exactly African startups raised in 2022, but from all indicators, it’s close to what was raised last year. Over $4 billion has been raised so far in 2022 according to <a href="https://thebigdeal.substack.com/p/2022-sets-yet-another-record" target="_blank" rel="noreferrer noopener">the Big Deal</a>.</p>



<p>While there was no unicorn minted this year, a number of notable investment deals were made. Tanzanian startup, Ramani, <a href="https://techcabal.com/2022/11/23/ramani-raises-32-million-series-a-to-digitise-tanzanias-supply-chain/" target="_blank" rel="noreferrer noopener">raised a $32 million</a> Series A, the largest Series A ever from the country; Wasoko (formerly Sokowatch), closed <a href="https://techcabal.com/2022/03/16/sokowatch-expands-to-west-africa/" target="_blank" rel="noreferrer noopener">a $125 million</a> Series B at a $625 million valuation;  Algerian Yassir raised <a href="https://techcabal.com/2022/11/07/yassir-raises-150m-series-b/" target="_blank" rel="noreferrer noopener">$150m</a> Series B;  Nigerian Fintech TeamApt raised<a href="https://techcabal.com/2022/08/11/qed-makes-its-first-investment-in-africa-through-teamapt/" target="_blank" rel="noreferrer noopener"> $50 million</a>; and Congo-based crypto startup Jambo raised <a href="https://www.coindesk.com/business/2022/05/10/paradigm-enters-africa-with-30m-round-for-super-app-jambo/" target="_blank" rel="noreferrer noopener">$37.5 million</a> cumulatively this year.</p>



<ol start="7"><li><strong>African companies embraced the Metaverse</strong></li></ol>



<p>In the past 12 months, the popularity of the Metaverse has soared with many companies making a play into the space through patents or experiments carried out.</p>



<p>In February, after its <a href="https://techcabal.com/2022/02/16/mtn-logo-new-telecoms-to-tech/" target="_blank" rel="noreferrer noopener">rebrand</a> Africa’s largest telco MTN <a href="https://techcabal.com/2022/02/28/mtn-buys-digital-land-first-african-company-to-enter-metaverse/" target="_blank" rel="noreferrer noopener">bought</a> 144 plots of digital land in the Africarare metaverse Ubuntuland for an undisclosed sum, becoming the first African company to do so. Later in the year, <a href="https://techcabal.com/2022/09/21/nedbank-metaverse-africarare/" target="_blank" rel="noreferrer noopener">Nedbank</a> and South African retail <a href="https://techcabal.com/2022/11/24/game-enters-metaverse/" target="_blank" rel="noreferrer noopener">Game</a>, also followed suit.</p>



<ol start="8"><li><strong>5G is here to stay, with more African countries getting access to this technology&nbsp;</strong></li></ol>



<p>For long 5G has been touted to revolutionise the connectivity space; some analysts predict that 5G will add an additional <a href="https://www.primebusiness.africa/5g-to-create-economic-value-worth-2-2-trn-by-2034/" target="_blank" rel="noreferrer noopener">$2.2 trillion</a> to Africa’s economy by 2034.  This has led many African countries to begin trials with Gabon starting as early as <a href="https://www.dw.com/en/is-africa-ready-for-5g/a-51474261" target="_blank" rel="noreferrer noopener">2019</a>, but few have commercially launched 5G. This can be largely attributed to challenges around spectrum regulation clarity, commercial viability, and deployment deadlines.</p>



<p>This year MTN launched its 5G services across <a href="https://techcabal.com/2022/09/02/5g-in-nigeria-heres-what-you-should-know-about-mtns-latest-disruption/" target="_blank" rel="noreferrer noopener">Nigeria</a> and <a href="https://techcabal.com/2022/11/28/mtn-zambia-5g/" target="_blank" rel="noreferrer noopener">Zambia</a> in the fourth quarter. Orange also launched 5G in <a href="https://techcabal.com/2022/11/14/orange-botswana-5g/" target="_blank" rel="noreferrer noopener">Botswana</a>. These commercial launches are a positive step forward as the continent battles with low citizen purchasing power of 5G-enabled smartphones and expensive internet.</p>



<ol start="9"><li><strong>Global tech companies set up African offices&nbsp;</strong></li></ol>



<p>A physical presence speaks volumes of an organisation’s commitment to a country. This year a number of global tech companies set up their first African offices.</p>



<p>In March, Microsoft <a href="https://nairametrics.com/2022/03/21/microsoft-opens-first-100-million-african-development-centre-in-lagos/" target="_blank" rel="noreferrer noopener">opened</a> a new African Development Centre at Ikoyi, Lagos. The centre, which is a $100 million investment by the multi-billion dollar firm, is where software engineering solutions are expected to be provided to Africa. </p>



<p>In April, Google <a href="https://techcabal.com/2022/04/19/googles-first-african-product-development-center/" target="_blank" rel="noreferrer noopener">announced</a> its first African development centre in Nairobi. The centre is expected to help create transformative products and services for people in Africa.</p>



<p>In April, Visa opened its <a href="https://techcabal.com/2022/04/07/visa-first-african-innovation-studio-in-kenya/" target="_blank" rel="noreferrer noopener">first African innovation studio</a> in Kenya. This facility will serve the sub-Saharan Africa region and joins a <a href="https://usa.visa.com/about-visa/global-innovation-centers.html" target="_blank" rel="noreferrer noopener">network of innovation centres</a> operated by Visa since 2016, in cities including London, Dubai, and Singapore. The Nairobi studio is the first in Africa and sixth globally.</p>



<p>In July, Bolt <a href="https://techcabal.com/2022/07/06/bolt-opens-african-headquarters-in/" target="_blank" rel="noreferrer noopener">launched</a> its first African headquarters in Nairobi, a regional hub for the seven African countries in which Bolt is operational—Kenya, Uganda, Tanzania, Nigeria, Ghana, South Africa, and Tunisia.</p>



<ol start="10"><li><strong>Techstars Accelerator programme returned to Africa after five years</strong></li></ol>



<p>In April, Techstars <a href="https://techcabal.com/2022/07/29/techstars-ceo-maelle-gavet-accelerators-interest-in-africa/" target="_blank" rel="noreferrer noopener">announced</a> the launch of the ARM Labs Lagos Techstars Accelerator Programme focused on helping fintech and proptech startups with products that serve an African audience.</p>



<p>The announcement signified a break from the five-year hiatus the accelerator with over $500 million assets under management (AUM) had taken in Africa. Techstars earlier ran an accelerator programme in South Africa from 2016 to 2017, in partnership with Barclays Bank where they invested in 21 startups, out of which three have been acquired, five have gone out of business, and 13 are still running.&nbsp;</p>



<ol start="11"><li><strong>Swvl became the first African company to get listed via SPAC&nbsp;&nbsp;</strong></li></ol>



<p>Egypt-born and Dubai-headquartered mobility startup, Swvl, merged with Queen’s Gambit Growth Capital in April at a valuation of $1.5 billion, becoming the first African startup to go public via a special purpose acquisition company (SPAC).</p>



<p>Since getting listed, however, Swvl’s valuation has crashed, and the startup is now valued at <a href="https://finance.yahoo.com/quote/SWVL/key-statistics/?guccounter=1&amp;guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&amp;guce_referrer_sig=AQAAAGL8KiDogqwQYlxzbbm1gLJxMEdeXnUBrPFDcVLYHzEFMmuzaw6C76_lqXkylSfqBb2jFAedzcJcX_46Put_4BpO9pib-m_R4Zr4rRZI4G0TlPYWnmfhJtcEFCgVjHwl9grCYezu9eOkageHAMKjdIR0k1EhsHx9hIsKNtFTVVJ-" target="_blank" rel="noreferrer noopener">less than $40 million</a>. </p>



<ol start="12"><li><strong>The race for African data centres and cloud continues</strong></li></ol>



<p>At the start of the year, Oracle, the world’s largest database management company, <a href="https://techcabal.com/2022/01/24/oracle-cloud-africa-first-africa-data-centre/" target="_blank" rel="noreferrer noopener">opened</a> its first cloud region (a cluster of data centres) in Africa. Other global cloud and database service providers followed suit later in the year.</p>



<p>In October, Google declared its <a href="https://techcabal.com/2022/10/06/google-cloud-region-south-africa/" target="_blank" rel="noreferrer noopener">intention</a> to establish the first African Google Cloud region in South Africa. Amazon Web Services (AWS) in November <a href="https://techcabal.com/2022/11/01/amazon-web-services-picks-lagos-second-african-office-%EF%BF%BC/" target="_blank" rel="noreferrer noopener">opened</a> its first office in Lagos, Nigeria, five years after its first office in Johannesburg was opened in 2017. In December, Liquid Intelligent Technologies officially launched operations in <a href="https://techcabal.com/2022/12/01/liquid-intelligent-technologies-launches-in-nigeria/" target="_blank" rel="noreferrer noopener">Nigeria</a>, having earlier expanded to <a href="https://techcabal.com/2022/08/22/liquid-inteligent-technologies-opens-office-mkushi-zambia/" target="_blank" rel="noreferrer noopener">Zambia</a> in August.</p>



<ol start="13"><li><strong>Amazon Prime Video became more pronounced in Nigeria</strong></li></ol>



<p>Amazon’s Prime Video has been strategically expanding its Nigerian content offering in the last few years, but this year pushed more aggressively with marketing and offering Nigerians the opportunity to pay for the service in local currency, the naira. Prime Video was previously unavailable to Nigerians, as many had to use <a href="https://techcabal.com/2021/06/14/ten-vpns-you-can-use-in-nigeria/">VPNs</a> to access it.</p>



<p>In January, the company struck a multi-year exclusive <a href="https://deadline.com/2022/01/amazon-licensing-deal-nigerian-production-company-anthill-studios-1234905306/" target="_blank" rel="noreferrer noopener">licensing deal with Anthill Studios</a>, a Lagos-based company behind a couple of well-received movies including Elevator Baby and Day of Destiny. A year ago, it closed a similar deal with Inkblot Studios which produced the commercially successful The Wedding Party films. </p>



<p>In June, Amazon Prime Video <a href="https://techcabal.com/2022/06/21/amazon-prime-video-commissions-nollywoods-nemsia-films-for-3-films/" target="_blank" rel="noreferrer noopener">commissioned</a> Nollywood’s Nemsia Films, makers of God Calling (2018) and Journey of an African Colony (2019), to produce three films.</p>



<p>Recently, Nigerian Highlife singer, Flavour, was <a href="https://tribuneonlineng.com/flavour-reportedly-pockets-3-million-from-amazon-for-his-biopic/" target="_blank" rel="noreferrer noopener">reported</a> to have signed an exclusive deal with the streamers for the release of a biopic. </p>



<p>With these moves, Amazon Prime Video joined Africa’s video-on-demand (VOD)&nbsp; streaming war.</p>



<ol start="14"><li><strong>Vodacom pulled the plug on its video streaming service</strong></li></ol>



<p>The entry of new players to the African VOD scene also means there were some exits. Video Play, a video streaming service launched by Vodacom in August 2015, was shut down in July 2022.</p>



<p>The services had over 1 million downloads on the Google Play Store alone and was made recently free. The company had in 2019 secured the rights to live-stream the English FA Cup on the service as well as securing rights to broadcast American film production studio company Metro-Goldwyn-Mayer (MGM)’s content in 2020.</p>



<p>The streaming service joins a lengthy list of South African streaming services by mobile network operators to be discontinued, as competition in the on-demand content streaming space continues to get tougher.</p>



<ol start="15"><li><strong>Google’s Africa internet cable arrives in Africa</strong></li></ol>



<p>Equiano, a subsea internet cable <a href="https://techcabal.com/2022/04/21/googles-internet-cable-in-nigeria/" target="_blank" rel="noreferrer noopener">running</a> through Portugal to South Africa, arrived in Africa in 2022. The cable runs through Togo, Nigeria, Namibia, and South Africa. It’s expected to become operational this month. </p>



<p>This project marks a milestone in Google’s plan to provide affordable internet access in Africa by building global infrastructure to help bring faster internet to more people and lower connectivity costs.</p>



<p>The project, which is named after Nigerian-born writer and abolitionist Olaudah Equiano, is expected to help support further digital transformation on the continent and accelerate economic growth with GDPs of Nigeria expected to rise by $10.1 billion, South Africa $7 billion and $260 million in Namibia.</p>



<p>Closely related to that, Elon Musk’s Starlink received <a href="https://techcabal.com/2022/05/27/elon-musks-starlink-internet-service-nigeria/" target="_blank" rel="noreferrer noopener">approval</a> to provide internet service in Nigeria and Mozambique.</p>



<ol start="16"><li><strong>Meta-backed 2Africa Subsea Cable internet lands in Africa</strong></li></ol>



<p>At 45,000km, 2Africa Pearls is the world’s largest subsea internet cable and is set to connect 33 locations at 46 locations across Africa, Europe, and Asia once it’s complete. In December, the cable <a href="https://techcentral.co.za/meta-backed-2africa-cable-comes-ashore-near-cape-town/218535/" target="_blank" rel="noreferrer noopener">landed</a> in Cape Town. The 2Africa project aims to provide Africa with better internet access.</p>



<p>Launched by Meta in May 2020, the 2Africa project is done in collaboration with MTN, Orange, Vodafone, and China Mobile. Unlike Equiano, the 2Africa cable will eventually encircle the entire African continent, with the first part of the system scheduled to go live next year.</p>



<ol start="17"><li><strong>Meta quietly shuts down its low-cost internet programme across Africa</strong></li></ol>



<p>After more than five years in operation, Meta <a href="https://techcabal.com/2022/02/08/meta-quietly-shuts-down-its-low-cost-internet-service-across-africa/" target="_blank" rel="noreferrer noopener">shut down</a> Express Wi-Fi, a programme designed to provide low-cost internet in developing countries through partnerships with local communities, mobile operators, and businesses. The Express Wi-Fi program was operational in countries such as  Nigeria, the Democratic Republic of Congo, Nigeria, Kenya, Côte d’Ivoire, Zambia, Cameroon, Ghana, Zimbabwe, Madagascar, South Africa, and Uganda.</p>



<ol start="18"><li><strong>Workplace culture issues and scandals</strong></li></ol>



<p>In addition to layoffs and the economic downturn, scandals rocked the booming African tech ecosystem in 2022.</p>



<p>This year saw a number of tech startup CEOs being challenged for misconduct.&nbsp;</p>



<p>In March 2022, the <a href="https://techcabal.com/2022/03/21/tyranny-in-the-workplace-the-chaotic-culture-of-bento-africa/" target="_blank" rel="noreferrer noopener">alleged toxic behaviour</a> of Ebunoluwa Okunbanjo, Bento Africa CEO, was exposed after a series of interviews with former and current employees. In light of these revelations, Okunbanjo was asked to step aside from the company for a few months by the board of directors. He later returned to the helm of the company as CEO.</p>



<p>In April, Flutterwave CEO Olugbenga Agboola was in the spotlight for a myriad of <a href="https://techcabal.com/2022/04/16/flutterwave-iyin-aboyeji-startup-ceo-accusation/" target="_blank" rel="noreferrer noopener">allegations</a> ranging from <a href="https://medium.com/@WanjikuClara/the-flutterwave-ceo-is-bullying-me-and-it-ends-today-b31e86321701" target="_blank" rel="noreferrer noopener">harassment</a> to insider trading, based on different revelations. Flutterwave has denied these allegations. Other notable startups that faced scandals include Egyptian B2B e-commerce <a href="https://techcrunch.com/2022/09/09/founders-of-well-funded-egyptian-b2b-startup-capiter-fired-following-fraud-allegations/" target="_blank" rel="noreferrer noopener">Capiter</a>, <a href="https://weetracker.com/2022/10/20/kloud-commerce-shuts-down/" target="_blank" rel="noreferrer noopener">Kloud Commerce</a>, <a href="https://techcabal.com/2022/10/06/investigation-into-risevest-ceo-finds-him-guilty-of-sexual-impropriety-and-abuse-of-power/#:~:text=A%20six%2Dweek%20investigation%20into,a%20statement%20shared%20with%20TechCabal." target="_blank" rel="noreferrer noopener">Risevest</a>, and <a href="https://techcabal.com/2022/11/19/healthlane-hospitals-obsolete-startup-battling-business/" target="_blank" rel="noreferrer noopener">Healthlane</a>.</p>



<ol start="19"><li><strong>A wave of acquisitions&nbsp;</strong></li></ol>



<p>There&#8217;s been a rise in acquisition deals happening on the continent this year. In the first half of 2022, TechCabal tracked 26 acquisitions; meanwhile, in Q3 2022, we tracked 17. Some of these acquisitions are: </p>



<p>B2B marketplace TradeDepot’s <a href="https://techcrunch.com/2022/02/23/b2b-marketplace-tradedepot-acquires-green-lion-to-accelerate-its-growth-in-ghana/" target="_blank" rel="noreferrer noopener">acquired</a> Accra-based GreenLion;  Silvertree’s $12.3 million <a href="https://techmoran.com/2022/02/24/silvertree-holdings-acquires-south-africas-meal-kit-delivery-ucook-for-12-3m/" target="_blank" rel="noreferrer noopener">acquired</a> South African meal kit delivery startup Ucook; MFS Africa’s $34 million <a href="https://techcabal.com/2022/06/07/mfs-africa-to-acquire-us-based-gtp-for-34-million/" target="_blank" rel="noreferrer noopener">bought</a> Global Technology Partners; Liquid Intelligent Technologies <a href="https://techcabal.com/2022/08/17/liquid-intelligent-technologies-completes-telrad-acquisition/" target="_blank" rel="noreferrer noopener">acquired</a> of Israeli Telrad; Belgium-based Dstyn’s <a href="https://weetracker.com/2022/06/08/egyptian-customer-experience-startup-tactful-ai-acquired-by-dstny/" target="_blank" rel="noreferrer noopener">purchased</a> Egyptian Tactful AI; Nigerian home concierge startup Eden life <a href="https://techcabal.com/2022/05/19/what-does-eden-lifes-expansion-to-kenya-mean-for-africas-gig-economy/" target="_blank" rel="noreferrer noopener">acquired</a> Kenyan-based Lynk; UK-based power company Bboxx <a href="https://techcabal.com/2022/04/27/bboxx-acquires-ghanas-peg-africa/" target="_blank" rel="noreferrer noopener">acquired</a> West Africa-based solar energy provider Peg; Moroccan B2B e-commerce Chari <a href="https://techcabal.com/2022/06/10/chari-acquires-diago/" target="_blank" rel="noreferrer noopener">acquired</a> Ivorian B2B e-commerce startup Diago;  and mPharma <a href="https://mpharma.com/2022/09/14/mpharma-acquires-majority-stake-in-healthplus/" target="_blank" rel="noreferrer noopener">acquired</a> a majority stake in HealthPlus. </p>



<ol start="20"><li><strong> A South African was charged in the largest fraud scheme involving bitcoin</strong></li></ol>



<p>In July, 2022, the U.S Commodities Futures Trading Commission (CFTC) <a href="https://techcabal.com/2022/07/11/south-african-charged-in-largest-bitcoin-fraud-scheme/" target="_blank" rel="noreferrer noopener">charged</a> South African resident Cornelius Johannes Steynberg in a bitcoin fraud scheme case totalling $1.7 billion. Sternberg was recently detained in Brazil on an Interpol arrest warrant. </p>



<ol start="21"><li><strong>&nbsp;Zanzibar launched Silicon Zanzibar&nbsp;</strong></li></ol>



<p>Zanzibar, a semi-autonomous island in East Africa, launched its plan to be Africa’s leading tech hub, through its Silicon Zanzibar project.</p>



<p>Led by the Zanzibar Ministry of Investment and Economic Development alongside several African tech companies, Silicon Zanzibar aims to attract technology firms and workers from across Africa and beyond. To lure tech companies, Zanzibar is dishing out work visas for relocating tech workers, something that has been problematic in mature markets like Nigeria, Kenya, Egypt, and South Africa.</p>



<p>Other incentives in the Zanzibar Free Economic Zone include exemption from corporate tax for 10 years.</p>



<ol start="22"><li><strong>MTN exits the Middle East</strong></li></ol>



<p>In November, Africa’s largest wireless carrier, MTN Group <a href="https://www.bloomberg.com/news/articles/2022-11-04/mtn-sells-afghan-unit-for-35-million-in-latest-middle-east-exit?leadSource=uverify%20wall" target="_blank" rel="noreferrer noopener">announced</a> that it sold its Afghanistan business to Beirut-based M1 New Ventures for $35 million as it continues to reduce its presence outside the continent. </p>



<p>This move is in line with MTN’s strategic priority, since 2020, of narrowing focus on its home continent. The group has earlier abandoned its Syrian business and transferred its Yemen unit to a partner. MTN remains present in Iran.</p>
                    <div class="social-widget social-share">
                        <span>Share this article</span>
                        <ul class="social-links">
    <li><a target="_blank" href="https://twitter.com/share?url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F&amp;text=22%20things%20that%20happened%20for%20the%20first%20time%20in%202022%20in%20the%20African%20tech%20scene" class="share-icon share-twitter" data-type="twitter"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png" alt="Twitter" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red@2x.png 2x"></a></li><li><a target="_blank" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F&amp;title=22%20things%20that%20happened%20for%20the%20first%20time%20in%202022%20in%20the%20African%20tech%20scene&amp;summary=Here%E2%80%99s%20a%20list%20of%2022%20things%20that%20happened%20for%20the%20first%20time%20in%20the%20African%20tech%20scene%20this%20year.%C2%A0" class="share-icon share-linkedin" data-type="linkedin"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png" alt="Linkedin" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red@2x.png 2x"></a></li><li><a target="_blank" href="https://api.whatsapp.com/send?text=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F" class="share-icon share-whatsapp" data-type="whatsapp"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red.png" alt="WhatsApp" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red@2x.png 2x"></a></li><li><a target="_blank" href="https://www.facebook.com/dialog/share?app_id=252296078952383&amp;display=popup&amp;href=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F" class="share-icon share-facebook" data-type="facebook"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png" alt="Facebook" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red@2x.png 2x"></a></li><li><a target="_blank" href="mailto:?body=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F30%2F22-things-first-time-in-2022-in-the-african-tech-scene%2F&amp;subject=22%20things%20that%20happened%20for%20the%20first%20time%20in%202022%20in%20the%20African%20tech%20scene" class="share-icon share-email" data-type="email"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red.png" alt="Email" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red@2x.png 2x"></a></li></ul>
                    </div>
                    <div class="author-widget">
                                            </div>
                    
<div id="list-newsletter-form" class="list-newsletter-form shortcode">
    <h2>Get the best African tech newsletters in your inbox</h2>
    <form class="newsletter-subscribe newsletter-signup-form columns" data-location="single-post">
        <input type=hidden name="fname" class="fname" required placeholder="First Name" class="firstname theheader__form__firstname">
        <input type="text" name="email" class="email" required placeholder="Your Email" class="email theheader__form__email">
        <div class="tc-newsletter-checkbox">
            <label class="checkbox">
                <span class="checkbox-input">
                    <input class="checkbox-input-elem" type="checkbox" name="list_tcdaily" value="107863888" checked>
                    <span class="checkbox-control">
                        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' aria-hidden="true" focusable="false">
                            <path fill='none' stroke='currentColor' stroke-width='3' d='M1.73 12.91l6.37 6.37L22.79 4.59' />
                        </svg>
                    </span>
                </span>
                <span class="checkbox-radio-label">TC Daily</span>
            </label>
            <label class="checkbox">
                <span class="checkbox-input">
                    <input class="checkbox-input-elem" type="checkbox" name="list_nextwave" value="107863897" checked>
                    <span class="checkbox-control">
                        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' aria-hidden="true" focusable="false">
                            <path fill='none' stroke='currentColor' stroke-width='3' d='M1.73 12.91l6.37 6.37L22.79 4.59' />
                        </svg>
                    </span>
                </span>
                <span class="checkbox-radio-label">Next Wave</span>
            </label>
            <label class="checkbox">
                <span class="checkbox-input">
                    <input class="checkbox-input-elem" type="checkbox" name="list_event" value="107863894" checked>
                    <span class="checkbox-control">
                        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' aria-hidden="true" focusable="false">
                            <path fill='none' stroke='currentColor' stroke-width='3' d='M1.73 12.91l6.37 6.37L22.79 4.59' />
                        </svg>
                    </span>
                </span>
                <span class="checkbox-radio-label">Events</span>
            </label>
            <label class="checkbox">
                <span class="checkbox-input">
                    <input class="checkbox-input-elem" type="checkbox" name="list_weekender" value="111174226" checked>
                    <span class="checkbox-control">
                        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' aria-hidden="true" focusable="false">
                            <path fill='none' stroke='currentColor' stroke-width='3' d='M1.73 12.91l6.37 6.37L22.79 4.59' />
                        </svg>
                    </span>
                </span>
                <span class="checkbox-radio-label">Weekender</span>
            </label>
        </div>
        <button type="button" class="theheader__form__submit border-button">Subscribe</button>
    </form>
</div>                    <div class="comment-section" style="margin-top: 40px;">
                        <div class="fb-comments-container"><div class="fb-comments" data-colorscheme="dark" data-href="https://techcabal.com/2022/12/30/22-things-first-time-in-2022-in-the-african-tech-scene/" data-width="800" data-numposts="10" style="max-width: 100%;" data-mobile="true"></div></div>                    </div>
                </div>
                <div class="list-sidebar" id="single-article-sidebar">
                    <div class="list-sidebar-item">
                        <div class="ad-box"><div class="ad" id="div-db-2"></div></div>                    </div>
                    <div class="list-sidebar-item">
                        <div class="list-trending list-small list-inverted">
                            <h2>More from this author</h2>
                                <div class="article-list-wrapper" data-columns="3">
        
<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/23/insights-from-africa-investors-in-2022/">
            <img width="83" height="55" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2021/12/Ask-an-Investor-the-year-in-review-240x160.jpg" class="attachment-90x55 size-90x55 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2021/12/Ask-an-Investor-the-year-in-review-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2021/12/Ask-an-Investor-the-year-in-review-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2021/12/Ask-an-Investor-the-year-in-review-760x506.jpg 760w" loading="lazy" sizes="(max-width: 83px) 100vw, 83px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/ask-an-investor/" class="article-list-category">Ask An Investor</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/23/insights-from-africa-investors-in-2022/" class="article-list-title">
            Ask an Investor: Twelve insights from Africa’s top investors in 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/daniel/" title="Posts by Daniel Adeyemi" rel="author">Daniel Adeyemi</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/22/fadilah-tchoumba-african-smes-startups-build-companies/">
            <img width="83" height="55" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Fadilah-Ask-an-Investor-240x160.jpg" class="attachment-90x55 size-90x55 wp-post-image" alt="Fadilah Tchoumba" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Fadilah-Ask-an-Investor-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Fadilah-Ask-an-Investor-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Fadilah-Ask-an-Investor-760x506.jpg 760w" loading="lazy" sizes="(max-width: 83px) 100vw, 83px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/ask-an-investor/" class="article-list-category">Ask An Investor</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/22/fadilah-tchoumba-african-smes-startups-build-companies/" class="article-list-title">
            How Fadilah Tchoumba is helping African SMEs and startups build investable companies        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/daniel/" title="Posts by Daniel Adeyemi" rel="author">Daniel Adeyemi</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/19/techstars-oyin-solebo-managing-director/">
            <img width="83" height="55" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Oyin-Solebo-1-240x160.jpeg" class="attachment-90x55 size-90x55 wp-post-image" alt="Oyin Solebo, Managing Director Techstars" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Oyin-Solebo-1-240x160.jpeg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Oyin-Solebo-1-480x320.jpeg 480w" loading="lazy" sizes="(max-width: 83px) 100vw, 83px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/news/" class="article-list-category">News</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/19/techstars-oyin-solebo-managing-director/" class="article-list-title">
            ARM Labs Lagos Techstars Accelerator appoints Oyin Solebo as Managing Director        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/daniel/" title="Posts by Daniel Adeyemi" rel="author">Daniel Adeyemi</a></span>
                                                            </div>
                </div>
    
</article>
    </div>
                            </div>
                    </div>
                    <div class="list-sidebar-item desktop">
                        <div class="ad-box"><div class="ad" id="div-db-3"></div></div>                    </div>
                    <div class="list-sidebar-item">
                        <div class="ad-box"><div class="ad" id="div-db-4"></div></div>                    </div>
                </div>
            </div>
        </article>
    </div>
</section>
<section class="article-list-section list-next">
    <div class="content">
        <div class="list-next-section">
            <div class="mobile">
                <h2>Read Next</h2>
            </div>
            
<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/08/etisalat-vodacom-acquisition/">
            <img width="1000" height="667" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat.jpeg" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="etisalat vodacom vodafone" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat.jpeg 1000w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat-300x200.jpeg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat-240x160.jpeg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat-768x512.jpeg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat-690x460.jpeg 690w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat-480x320.jpeg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/etisalat-760x506.jpeg 760w" loading="lazy" sizes="(max-width: 1000px) 100vw, 1000px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/news/" class="article-list-category">News</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/08/etisalat-vodacom-acquisition/" class="article-list-title">
            Etisalat mulling over acquisition of Vodafone’s Vodacom stake        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/ephraim/" title="Posts by Ephraim Modise" rel="author">Ephraim Modise</a></span>
                                                            </div>
                </div>
    
</article>
        </div>
    </div>
</section>
        <section class="article-list-section list-readmore" id="read-more">
            <div class="content">
                <div class="list-readmore-wrapper">
                    <h2>Read more</h2>
                        <div class="article-list-wrapper" data-columns="6">
        
<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/11/22/startup-acquisitions-in-african-tech-grow-by-41-in-q3-2022/">
            <img width="240" height="160" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/the_state_of_tech_in_africa_q3-01-1-240x160.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/the_state_of_tech_in_africa_q3-01-1-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/the_state_of_tech_in_africa_q3-01-1-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/the_state_of_tech_in_africa_q3-01-1-760x506.jpg 760w" loading="lazy" sizes="(max-width: 240px) 100vw, 240px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/african-tech-roundup/" class="article-list-category">African Tech Roundup</a>
                                            </div>
                        <a href="https://techcabal.com/2022/11/22/startup-acquisitions-in-african-tech-grow-by-41-in-q3-2022/" class="article-list-title">
            Startup acquisitions in African tech grew by 41% in Q3 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/damilola-makinde/" title="Posts by Damilola Makinde" rel="author">Damilola Makinde</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/11/02/leading-tech-moves-october/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/May-2022-5-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="african tech moves" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/May-2022-5-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/May-2022-5-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/11/May-2022-5-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/african-tech-roundup/" class="article-list-category">African Tech Roundup</a>
                                            </div>
                        <a href="https://techcabal.com/2022/11/02/leading-tech-moves-october/" class="article-list-title">
            The leading African tech moves from October 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/09/05/leading-tech-moves-august/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/09/May-2022-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="African tech August 2022" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/09/May-2022-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/09/May-2022-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/09/May-2022-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/african-tech-roundup/" class="article-list-category">African Tech Roundup</a>
                                            </div>
                        <a href="https://techcabal.com/2022/09/05/leading-tech-moves-august/" class="article-list-title">
            The leading African tech moves from August 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/08/24/the-state-of-tech-in-africa-quick-review-of-h1-2022/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/State-of-techxxx-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/State-of-techxxx-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/State-of-techxxx-480x320.jpg 480w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/african-tech-roundup/" class="article-list-category">African Tech Roundup</a>
                                            </div>
                        <a href="https://techcabal.com/2022/08/24/the-state-of-tech-in-africa-quick-review-of-h1-2022/" class="article-list-title">
            The State of Tech in Africa: Quick review of H1 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/fikayo/" title="Posts by Fikayo Idowu" rel="author">Fikayo Idowu</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/08/05/the-leading-tech-moves-from-july/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/May-2022-1-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/May-2022-1-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/May-2022-1-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/08/May-2022-1-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/african-tech-roundup/" class="article-list-category">African Tech Roundup</a>
                                            </div>
                        <a href="https://techcabal.com/2022/08/05/the-leading-tech-moves-from-july/" class="article-list-title">
            The leading African tech moves from July 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/07/05/the-biggest-african-tech-moves-from-june-2022/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/May-2022-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/May-2022-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/May-2022-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/May-2022-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/african-tech-roundup/" class="article-list-category">African Tech Roundup</a>
                                            </div>
                        <a href="https://techcabal.com/2022/07/05/the-biggest-african-tech-moves-from-june-2022/" class="article-list-title">
            The leading African tech moves from June 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>
    </div>
                    </div>
                <div class="list-sidebar">
                    <div class="ad-box"><div class="ad" id="div-db-5"></div></div>                </div>
            </div>
        </section>
<section style="margin: 30px 0 60px">
    <div class="content">
        <div class="desktop">
            <a style="display: inline-block;" target="_blank" href="https://techcabal.com/newsletter"><img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/large_newsletter_banner_new.jpg" width="100%" height="auto" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/large_newsletter_banner_new.jpg 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/large_newsletter_banner_new@2x.jpg 2x"></a>
        </div>
        <div style="margin: 40px auto 0; text-align: center;" class="mobile">
            <a style="display: inline-block;" target="_blank" href="https://techcabal.com/newsletter"><img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mpu-newsletter-new.jpg" width="300" height="250" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mpu-newsletter-new.jpg 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mpu-newsletter-new@2x.jpg 2x"></a>
        </div>
    </div>
</section>
</main>
</div>
<footer id="footer" class="footer">
    <div class="content">
        <div class="footer-left">
            <div class="logo">
                <a href="/"><img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop.png" width="210" height="45" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tclogo-desktop@2x.png 2x" alt="TechCabal"></a>
            </div>
            <div class="site-desc">
                TechCabal is a future-focused publication that speaks to African innovation and technology in depth
            </div>
        </div>
        <div class="footer-right">
            <div class="social-widget social-follow">
                <span>Follow us</span>
                <ul class="social-links">
    <li><a href="https://twitter.com/TechCabal" target="_blank" class="social-icon social-twitter"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png" alt="Twitter" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red@2x.png 2x"></a></li><li><a href="https://www.linkedin.com/company/techcabal/" target="_blank" class="social-icon social-linkedin"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png" alt="Linkedin" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red@2x.png 2x"></a></li><li><a href="https://www.facebook.com/TechCabal/" target="_blank" class="social-icon social-facebook"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png" alt="Facebook" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red@2x.png 2x"></a></li><li><a href="https://www.instagram.com/techcabal/" target="_blank" class="social-icon social-instagram"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/instagram_red.png" alt="Instagram" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/instagram_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/instagram_red@2x.png 2x"></a></li><li><a href="https://www.youtube.com/user/TechCabal" target="_blank" class="social-icon social-youtube"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/youtube_red.png" alt="Youtube" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/youtube_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/youtube_red@2x.png 2x"></a></li></ul>            </div>
            <div class="site-copyright">
                <a href="/"><img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/bcm-logo.png" width="50" height="50" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/bcm-logo.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/bcm-logo@2x.png 2x" alt="BigCabal"></a>
                <div class="site-copyright-text">Copyright ©2022. All rights reserved. Privacy & Terms.</div>
            </div>
        </div>
    </div>
</footer>
<div class="download-modal-bg" id="report-modal" style="display:none;">
    <div class="download-modal">
        <div class="close-modal">&times;</div>
        <div id="model-form">
            <div class="logo-image-holder">
                <a href="/tcinsights">
                    <img loading="lazy" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-insights-logo.png" width="145" height="auto" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-insights-logo.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/tc-insights-logo@2x.png 2x">
                </a>
            </div>
            <div class="download-report-info">
                <div class="download-report-img">
                    <img width="125" height="150" src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/report-placeholder.png" class="wp-post-image" alt="report title"/>
                </div>
                <div>
                    <h1 class="download-report-title">TechCabal’s 2021 Year-End report</h1>
                    <p class="download-report-offer">Free</p>
                </div>
            </div>
            <div class="download-report-wrapper">
                <form class="report-download-form">
                    <label>
                        <input type="text" name="first-name" class="first-name" placeholder="First Name"/>
                    </label>
                    <label>
                        <input type="text" name="last-name" class="last-name" placeholder="Last Name"/>
                    </label>
                    <label>
                        <input type="email" name="work-email" class="work-email" placeholder="Work Email"/>
                    </label>
                    <label>
                        <input type="text" name="company" class="company" placeholder="Company"/>
                    </label>
                    <label>
                        <input type="text" name="job-title" class="job-title" placeholder="Job Title"/>
                    </label>
                    <label class="checkbox" for="send-report-emails">
                    <span class="checkbox-field">
                        <input type="checkbox" name="send-report-emails" id="send-report-emails" value="111752635" class="checkbox-input-elem" checked/>
                        <span class="checkbox-control">
                            <svg width="10" height="7" viewBox="0 0 10 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M3.75 6.66907L0.625 3.56907L1.61875 2.60657L3.75 4.70032L8.38125 0.106567L9.375 1.09407L3.75 6.66907Z" fill="#6C6C6C"/>
                            </svg>
                        </span>
                    </span>
                        <span class="checkbox-label">Send me emails about TechCabal Reports and other Insights</span>
                    </label>
                    <label  class="checkbox" for="newsletter-subscriptions">
                    <span class="checkbox-field">
                        <input type="checkbox" name="newsletter-subscription" id="newsletter-subscription" value="109788065" class="checkbox-input-elem" checked/>
                        <span class="checkbox-control">
                            <svg width="10" height="7" viewBox="0 0 10 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M3.75 6.66907L0.625 3.56907L1.61875 2.60657L3.75 4.70032L8.38125 0.106567L9.375 1.09407L3.75 6.66907Z" fill="#6C6C6C"/>
                            </svg>
                        </span>
                    </span>
                        <span class="checkbox-label">Sign me up for TechCabal’s Daily Newsletters</span>
                    </label>
                    <input type="submit" class="submit-button" value="Get the Report"/>
                </form>
            </div>
        </div>
        <div id="modal-form-success">
            <div>
                <img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/icon-park_email-successfully.png">
                <h1>Success!</h1>
                <p>Check your email for your report</p>
                <a class="submit-button" href="/reports">Get More Reports</a>
            </div>
        </div>
    </div>
</div><template id="category-article-list-item">
    <article class="article-list-item" data-href="">
        <div class="article-list-img"></div>
        <div class="article-list-desc">
            <a href="" class="article-list-category"></a>
            <a href="" class="article-list-title"></a>
            <div class="article-list-meta">
                <span class="article-list-author"></span>
                <span class="article-list-date"></span>
            </div>
        </div>
    </article>
</template>
<template id="download-report-form-success-template">
    <div class="report-form-success" data-href="">
        <div class="report-form-success-img">
            <svg width="130" height="101" viewBox="0 0 130 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M127.5 49V2.125H65H2.5V49V95.875H65" stroke="#FA5129" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M86.875 86.5L102.5 99L127.5 67.75" stroke="#FA5129" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2.5 2.125L65 49L127.5 2.125" stroke="#FA5129" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        <div class="report-form-success-text">
            <p class="report-form-success-text">Check your email for your report</p>
            <a href="https://techcabal.com/reports" class="button report-form-success-link">Get More Reports</a>
        </div>
    </div>
</template>        <script>
            var googletag = googletag || {};
            googletag.cmd = googletag.cmd || [];

            googletag.cmd.push(function() {
                var sizemap = null;
                sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[970,90],[970,250],[728,90]]).addSize([ 300, 0 ], [[320,50],[300,100],[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc-homepage-top-leaderboard', [[970,90],[970,250],[728,90],[320,50],[300,100],[300,250]], 'div-db-0').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_300_new_2', [[300,250],[300,250]], 'div-db-1').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,600],[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_rectangle_new', [[300,600],[300,250],[300,250]], 'div-db-2').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_300_new_2', [[300,250],[300,250]], 'div-db-3').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_300_new_2', [[300,250],[300,250]], 'div-db-4').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_300_new_2', [[300,250],[300,250]], 'div-db-5').defineSizeMapping(sizemap).addService(googletag.pubads());            });

            googletag.cmd.push(function() {
                var pageConfig = {
                    allowOverlayExpansion: true,
                    allowPushExpansion: true,
                    sandbox: true
                };
                googletag.pubads().setSafeFrameConfig(pageConfig);
                googletag.pubads().enableSingleRequest();
                googletag.enableServices();
            });
        </script>
                <script>
            googletag.cmd.push(function() {                if (document.getElementById('div-db-0')) {
                    googletag.display('div-db-0');
                }                if (document.getElementById('div-db-1')) {
                    googletag.display('div-db-1');
                }                if (document.getElementById('div-db-2')) {
                    googletag.display('div-db-2');
                }                if (document.getElementById('div-db-3')) {
                    googletag.display('div-db-3');
                }                if (document.getElementById('div-db-4')) {
                    googletag.display('div-db-4');
                }                if (document.getElementById('div-db-5')) {
                    googletag.display('div-db-5');
                }            });
        </script>
        <script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/js/main.min.js?ver=7.0.1' id='main-script-js'></script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/js/pwa.min.js?ver=7.0.1' id='pwa-script-js'></script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/js/news-tagging.min.js?ver=2.0' id='news-tag-js'></script>
<script type='text/javascript' src='https://cdn.onesignal.com/sdks/OneSignalSDK.js?ver=6.0.2' async='async' id='remote_sdk-js'></script>
</body>
</html>
''')
print(data)