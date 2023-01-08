import re

from app.tools.parser import Parser

# inp = '''
# \n#h1#Why Future Africa and TLG Capital just created a $25 million debt financing programme@h1@\n\n#p##img# src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/Future-Africa.webp" @img@@p@\n\n#p#                                        Image source: Techcabal                                    @p@'''
# html_to_text = re.sub(r"(.*)#p##img#.*src=(.*)@img@@p@(.*)", f"\g<1><img src=\g<2> />\g<3><div class='text-small d-inline image-source'><i>TechCabal</i></div>",
#                                    inp)
# print(html_to_text)



parser = Parser(
   {
      "url": "https://techcabal.com/",
      "h1": [
         [
            "h1",
            "class",
            "single-article-title",
            "0"
         ],
         "text"
      ],
      "date": [
         [
            "span",
            "class",
            "single-article-date",
            "0"
         ],
         "text"
      ],
      "date_engine": [
         "_january_01_1970"
      ],
      "description": [
         [
            "meta",
            "property",
            "og:description",
            "0"
         ],
         "content"
      ],
      "main_content": [
         [
            "main",
            "",
            "",
            2
         ],
         "contents"
      ],
      "terminator": "Share this article",
      "unwanted_blocks": [
         [
            [
               "div",
               "class",
               "single-article-info",
               "0"
            ],
            "tag",
            True
         ],
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
      "bad_signatures": [[["div", "class", "single-article-category", "0"], "text", "newsletters"]],
      "image_source": "TechCabal"
   }
)
data = parser.extract('', '''

<!doctype html>
<html lang="en-US" class="no-js">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="pingback" href="https://techcabal.com/xmlrpc.php">
    
    <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO plugin v19.6.1 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>Understanding the concept of startups | TechCabal</title>
	<link rel="canonical" href="http://techcabal.com/2022/12/23/understanding-the-concept-of-startups/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Understanding the concept of startups | TechCabal" />
	<meta property="og:description" content="Startups are fledgling businesses that aim to develop and provide a novel product or service to the market in order to attract and retain customers. Read more to understand the concept of startups." />
	<meta property="og:url" content="http://techcabal.com/2022/12/23/understanding-the-concept-of-startups/" />
	<meta property="og:site_name" content="TechCabal" />
	<meta property="article:publisher" content="https://www.facebook.com/TechCabal" />
	<meta property="article:published_time" content="2022-12-23T07:00:00+00:00" />
	<meta property="article:modified_time" content="2022-12-22T14:54:07+00:00" />
	<meta property="og:image" content="https://lh6.googleusercontent.com/aIN3WLbZA_kSjZg8acmQcfZjIn_OfNqvHqiWJCU4PkMqHd65jI5IBvGZQmKzAJABpv4uj3YKMOiPphAcq_dK17Z6w5EyOhOP19Vu5F9RO73oaxwNBqVHXebP0wyI4c_boBTTBxufDvPt25ejfuBJFwt8RJOh-egj2nCFgtfMX-6ntpZxf4U_pW1VPSCU1Q" />
	<meta name="author" content="Damilola Makinde" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@techcabal" />
	<meta name="twitter:site" content="@techcabal" />
	<meta name="twitter:label1" content="Written by" />
	<meta name="twitter:data1" content="Damilola Makinde" />
	<meta name="twitter:label2" content="Est. reading time" />
	<meta name="twitter:data2" content="4 minutes" />
	<!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Feed" href="https://techcabal.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Comments Feed" href="https://techcabal.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Understanding the concept of startups Comments Feed" href="https://techcabal.com/2022/12/23/understanding-the-concept-of-startups/feed/" />
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
{"sampling_active":0,"sampling_rate":100,"ajax_url":"https:\/\/techcabal.com\/wp-json\/wordpress-popular-posts\/v1\/popular-posts","api_url":"https:\/\/techcabal.com\/wp-json\/wordpress-popular-posts","ID":105001,"token":"1526abd7cd","lang":0,"debug":0}
</script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/plugins/wordpress-popular-posts/assets/js/wpp.min.js?ver=6.0.5' id='wpp-js-js'></script>
<link rel="https://api.w.org/" href="https://techcabal.com/wp-json/" /><link rel="alternate" type="application/json" href="https://techcabal.com/wp-json/wp/v2/posts/105001" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://techcabal.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://techcabal.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 6.0.2" />
<link rel='shortlink' href='https://techcabal.com/?p=105001' />
<link rel="alternate" type="application/json+oembed" href="https://techcabal.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://techcabal.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F&#038;format=xml" />
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
                'author' : "Damilola Makinde",
                'pagetitle' : "Understanding the concept of startups",
                'publishdate' : "2022-12-23"
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

<body class="post-template-default single single-post postid-105001 single-format-standard  section-single"><div id="fb-root"></div>
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
    <div class="menu-wrapper"><ul class="menu"><li><a href="https://techcabal.com/tag/africa/">Africa</a></li><li><a href="https://techcabal.com/tag/startup/">Startup</a></li></ul></div></div>
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
<script type='application/ld+json'>{"@context":"https:\/\/schema.org\/","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/techcabal.com\/2022\/12\/23\/understanding-the-concept-of-startups\/"},"headline":"Understanding the concept of startups","image":[false],"datePublished":"2022-12-23T08:00:00+01:00","dateModified":"2022-12-22T15:54:07+01:00","author":{"@type":"Person","name":"Damilola Makinde"},"publisher":{"@type":"Organization","url":"https:\/\/techcabal.com","name":"TechCabal","logo":"https:\/\/x7d4c5z5.stackpathcdn.com\/wp-content\/themes\/tc1.5\/images\/tclogo-desktop.png"}}</script><section class="single-article">
    <div class="content">
        <article>
            <div class="single-article-meta">
                <div class="single-article-category">
                    <a href="https://techcabal.com/category/startups/">startups</a>
                </div>
                <h1 class="single-article-title">Understanding the concept of startups</h1>
                <div class="single-article-info">
                    <span class="single-article-author">By
                                                        <a href="https://techcabal.com/author/damilola-makinde/" title="Posts by Damilola Makinde" rel="author">Damilola Makinde</a>                                                </span>
                    <span class="single-article-date">Dec 23, 2022</span>
                </div>
                            </div>
            <div class="single-article-main">
                <div class="single-article-content" id="single-article">
                   <div class="wp-block-image">
<figure class="aligncenter"><img 
     	loading="lazy" src="https://lh6.googleusercontent.com/aIN3WLbZA_kSjZg8acmQcfZjIn_OfNqvHqiWJCU4PkMqHd65jI5IBvGZQmKzAJABpv4uj3YKMOiPphAcq_dK17Z6w5EyOhOP19Vu5F9RO73oaxwNBqVHXebP0wyI4c_boBTTBxufDvPt25ejfuBJFwt8RJOh-egj2nCFgtfMX-6ntpZxf4U_pW1VPSCU1Q" alt="startups "/></figure></div>


<p>Startups are organisations with the grand ambition to alter existing markets and create a better society. Startup initiators usually look to solve a problem in the world by creating a product or service that people want but doesn&#8217;t currently exist, ultimately leading to a successful initial public offering (IPO) and stratospheric returns for investors.</p>



<p>Startups are fledgling businesses that aim to develop and provide a novel product or service to the market in order to attract and retain customers. You can also refer to a startup as a disruptor or up-and-coming company that uses cutting-edge ideas to improve upon established products and services or to introduce totally new product categories that shake up established markets.&nbsp;</p>



<p>Popular examples of <a href="https://techcabal.com/2022/12/13/founding-startups-in-africa/">startups in Africa</a> include Paystack, Piggyvest, Boomplay, Risevest, and Pocket App. International ones include <a href="https://www.google.com/aclk?sa=l&amp;ai=DChcSEwj6mY-xuY38AhXW7XcKHbLwCYUYABAAGgJlZg&amp;ase=2&amp;sig=AOD64_2IGKjJjvfU1P5lWaLdgq9YTjIkFA&amp;q&amp;nis=4&amp;adurl&amp;ved=2ahUKEwiDxYSxuY38AhUvg_0HHXkVCVYQ0Qx6BAgJEAE">Amazon</a>, Netflix, and so on. </p>



<h2><strong>What&#8217;s the procedure for launching a startup?</strong></h2>



<p>There are several things you need to know before kick-starting a startup. First, a startup is not an abstract body. It operates similarly to any other established company, only maybe in a smaller company. Just like in other companies, startup employees collaborate to design a product they&#8217;re confident will sell.&nbsp;</p>



<p>However, most regular new businesses simply repeat what has already been done. This means that they follow a predetermined model for how a company should operate.</p>



<p>The goal of a startup is to establish a new standard. This entails offering a scale that existing providers of their product of service can&#8217;t immediately provide.</p>



<h2><strong>Rapid expansion: The goal of startups</strong></h2>



<p>Rapid expansion is another hallmark of successful startups that sets them apart from more established businesses. The goal of a startup is to rapidly implement ingenious ideas.&nbsp;</p>



<p>Startups engage several techniques such as iteration to collect user opinions and use that information to tweak and refine their products over time. You&#8217;ll find startups using the bare framework of a product to test and iterate on until it&#8217;s ready to release to the public.</p>



<p>In tandem with developing better products, startup companies want to quickly increase their consumer density too. They operate with the principle of establishing higher market shares to pursue further funding. This disposition helps the company expand its offerings and its customer base. Taking a company public is the end goal of all this fast expansion and innovation.&nbsp;</p>



<h2><strong>Funding startups</strong></h2>



<p><a href="https://techcabal.com/2022/12/12/why-your-startup-may-not-get-funding/">Funding</a> for new businesses typically occurs in stages. When the company&#8217;s founders and their close associates put up initial capital, this is called the &#8220;bootstrapping&#8221; round. The next step is to secure seed capital from external investors, or wealthy individuals who make such inception business investments.</p>



<p>The subsequent fundraising rounds range from tens of millions to hundreds of millions of dollars and are headed by venture capital firms. In the end, a startup may opt to go public and raise capital through an initial public offering (IPO), an acquisition by a special intention company, or stock exchange direct listing.&nbsp;</p>



<p>When a firm goes public, anyone can buy shares, and the startup&#8217;s original investors and backers can cash out for a huge profit.</p>



<p>But startups can fail. In other words, it&#8217;s entirely possible that inception investors will receive absolutely no return on their money.</p>



<h2><strong>Successfully launching a Startup: What makes a difference?</strong></h2>



<p>Many factors need to be in place, and important questions must be answered, for a business to be successful. However, a large percentage of startups don&#8217;t fly. Therefore the following positions need clear definition if a startup will thrive.&nbsp;&nbsp;</p>



<p>The following are general questions to query the startup idea:</p>



<h4><strong>What&#8217;s the size of the market?</strong></h4>



<p>Opportunity for a startup is proportional to the size of its potential market.&nbsp;</p>



<h4><strong>What&#8217;s the intention of the tech edge your startup may have?</strong></h4>



<p>While specialised technology may give one company a competitive edge over another, the question remains: for what purpose? To what end?</p>



<p>The following are questions for the founders:</p>



<h4><strong>Where is the founder&#8217;s experience in the field?</strong>&nbsp;</h4>



<p>It is imperative that the founders are well-versed in their startup&#8217;s industry. Founding a startup requires knowledge of certain things. Founders must be able to break down the aims of the company.&nbsp;&nbsp;</p>



<p>The need for the big idea must be explicit. What makes it worth the time of workers and the attention of employees? What sets apart the startup&#8217;s competition? Founders need to get a hang of all these variables.</p>



<h4><strong>Are team members completely invested in the project?</strong>&nbsp;</h4>



<p>Without a committed team behind it, even a fantastic idea risks falling flat with its intended audience. Successful completion is crucial.</p>



<h4><strong>Does it look like they&#8217;re willing to put in the effort?</strong>&nbsp;</h4>



<p>A team can be committed, but can they invest long hours to get the idea flying and keep it soaring? It can be difficult for a concept to succeed if the team working on it isn&#8217;t prepared to spend the majority of their time on it.</p>



<p>It&#8217;s possible that any startup type can join the few early stage ones that succeed, if it can provide satisfactory responses to these questions.</p>



<h2><strong>What to know about funding startups</strong></h2>



<p>Honestly, access to startup funding is limited. Therefore, you may need to start with your own money. However, later, you can work towards getting a private investor, VC or grant organisations to fund your business. But for a start, bootstrapping may be the way.</p>
                    <div class="social-widget social-share">
                        <span>Share this article</span>
                        <ul class="social-links">
    <li><a target="_blank" href="https://twitter.com/share?url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F&amp;text=Understanding%20the%20concept%20of%20startups" class="share-icon share-twitter" data-type="twitter"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png" alt="Twitter" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red@2x.png 2x"></a></li><li><a target="_blank" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F&amp;title=Understanding%20the%20concept%20of%20startups&amp;summary=Startups%20are%20fledgling%20businesses%20that%20aim%20to%20develop%20and%20provide%20a%20novel%20product%20or%20service%20to%20the%20market%20in%20order%20to%20attract%20and%20retain%20customers.%20Read%20more%20to%20understand%20the%20concept%20of%20startups." class="share-icon share-linkedin" data-type="linkedin"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png" alt="Linkedin" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red@2x.png 2x"></a></li><li><a target="_blank" href="https://api.whatsapp.com/send?text=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F" class="share-icon share-whatsapp" data-type="whatsapp"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red.png" alt="WhatsApp" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red@2x.png 2x"></a></li><li><a target="_blank" href="https://www.facebook.com/dialog/share?app_id=252296078952383&amp;display=popup&amp;href=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F" class="share-icon share-facebook" data-type="facebook"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png" alt="Facebook" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red@2x.png 2x"></a></li><li><a target="_blank" href="mailto:?body=https%3A%2F%2Ftechcabal.com%2F2022%2F12%2F23%2Funderstanding-the-concept-of-startups%2F&amp;subject=Understanding%20the%20concept%20of%20startups" class="share-icon share-email" data-type="email"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red.png" alt="Email" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red@2x.png 2x"></a></li></ul>
                    </div>
                    <div class="author-widget">
                        
        <div class="author-box">
            <div class="author-box-img">
                <a href="https://techcabal.com/author/damilola-makinde/">
                    <img alt='' src='https://secure.gravatar.com/avatar/33ef4d7a34ec110e8f82c6ed9dd2dee4?s=96&#038;d=mm&#038;r=g' srcset='https://secure.gravatar.com/avatar/33ef4d7a34ec110e8f82c6ed9dd2dee4?s=192&#038;d=mm&#038;r=g 2x' class='avatar avatar-96 photo' height='96' width='96' loading='lazy'/>                </a>
            </div>
            <div class="author-box-info">
                <div class="author-box-fullname"><strong>Damilola Makinde</strong> <span>Author</span></div>
                            </div>
        </div>
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
                        <div class="fb-comments-container"><div class="fb-comments" data-colorscheme="dark" data-href="https://techcabal.com/2022/12/23/understanding-the-concept-of-startups/" data-width="800" data-numposts="10" style="max-width: 100%;" data-mobile="true"></div></div>                    </div>
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
        <a href="https://techcabal.com/2022/12/24/5-major-reasons-your-phone-wont-charge-fast/">
            <img width="240" height="160" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/android-phone-charging-240x160.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/android-phone-charging-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/android-phone-charging-480x320.jpg 480w" loading="lazy" sizes="(max-width: 240px) 100vw, 240px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/consumer-tech/" class="article-list-category">Consumer Tech</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/24/5-major-reasons-your-phone-wont-charge-fast/" class="article-list-title">
            5 major reasons your phone won&#8217;t charge fast        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/damilola-makinde/" title="Posts by Damilola Makinde" rel="author">Damilola Makinde</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/24/breaking-your-phone-addiction-in-four-ways/">
            <img width="240" height="160" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-1-240x160.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-1-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-1-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-1-760x506.jpg 760w" loading="lazy" sizes="(max-width: 240px) 100vw, 240px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/consumer-tech/" class="article-list-category">Consumer Tech</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/24/breaking-your-phone-addiction-in-four-ways/" class="article-list-title">
            Breaking your phone addiction in four ways        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/damilola-makinde/" title="Posts by Damilola Makinde" rel="author">Damilola Makinde</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/23/buying-a-used-iphone-look-out-for-these-things/">
            <img width="240" height="160" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/lkjhgf-240x160.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/consumer-tech/" class="article-list-category">Consumer Tech</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/23/buying-a-used-iphone-look-out-for-these-things/" class="article-list-title">
            Buying a used iPhone? Look out for these things        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/damilola-makinde/" title="Posts by Damilola Makinde" rel="author">Damilola Makinde</a></span>
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
        <a href="https://techcabal.com/2022/12/22/marketing-strategies-that-worked-in-2022/">
            <img width="2560" height="1707" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-scaled.jpg" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-scaled.jpg 2560w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-300x200.jpg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-1024x683.jpg 1024w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-768x512.jpg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-1536x1024.jpg 1536w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-2048x1365.jpg 2048w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-690x460.jpg 690w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-1050x700.jpg 1050w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/campaign-creators-yktK2qaiVHI-unsplash-760x506.jpg 760w" loading="lazy" sizes="(max-width: 2560px) 100vw, 2560px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/consumer-tech/" class="article-list-category">Consumer Tech</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/22/marketing-strategies-that-worked-in-2022/" class="article-list-title">
            Marketing strategies that worked in 2022        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/anon/" title="Posts by Guest Author" rel="author">Guest Author</a></span>
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
        <a href="https://techcabal.com/2022/12/25/venture-capital-in-africa-2022/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/looking_back_african_venture_capital_2022_rhamely_unsplash-1-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="Am upside-down glass with a tiny Christmas tree in it." loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/looking_back_african_venture_capital_2022_rhamely_unsplash-1-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/looking_back_african_venture_capital_2022_rhamely_unsplash-1-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/looking_back_african_venture_capital_2022_rhamely_unsplash-1-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/startups/" class="article-list-category">startups</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/25/venture-capital-in-africa-2022/" class="article-list-title">
            2022: Venture capital in Africa        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/abraham/" title="Posts by Abraham Augustine" rel="author">Abraham Augustine</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/21/foundational-investing-techstars-latest-cohort-show-the-accelerators-strategic-approach-to-investment-in-africa/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-300x200.jpg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-768x513.jpg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-690x461.jpg 690w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144-760x506.jpg 760w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/OBA_9144.jpg 1000w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/ecosystem/" class="article-list-category">ecosystem</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/21/foundational-investing-techstars-latest-cohort-show-the-accelerators-strategic-approach-to-investment-in-africa/" class="article-list-title">
            Techstars&#8217; latest cohort show the accelerator’s approach to investment in Africa        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/caleb/" title="Posts by Caleb Nnamani" rel="author">Caleb Nnamani</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/15/ventures-platform-closes-its-pan-african-fund-at-46-million/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-300x200.jpg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-1024x683.jpg 1024w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-768x512.jpg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-1536x1024.jpg 1536w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-2048x1365.jpg 2048w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-690x460.jpg 690w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-1050x700.jpg 1050w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/L-R-_-Dr.-Dotun-Olowoporoku-and-Kola-Aina-Ventures-Plaform-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/funding/" class="article-list-category">Funding</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/15/ventures-platform-closes-its-pan-african-fund-at-46-million/" class="article-list-title">
            Ventures Platform closes its pan-African fund at $46 million        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/muktar/" title="Posts by Muktar Oladunmade" rel="author">Muktar Oladunmade</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/15/kenyan-healthtech-startup-myhealth-africa-raises-1-million/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/MyHealth-Africa-team-min-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/MyHealth-Africa-team-min-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/MyHealth-Africa-team-min-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/MyHealth-Africa-team-min-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/funding/" class="article-list-category">Funding</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/15/kenyan-healthtech-startup-myhealth-africa-raises-1-million/" class="article-list-title">
            Kenyan healthtech startup, MyHealth Africa, raises $1 million        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/muktar/" title="Posts by Muktar Oladunmade" rel="author">Muktar Oladunmade</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/13/nala-expands-into-europe-to-enable-cross-border-payments/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/NALA-team-photo-e1671005081868-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/NALA-team-photo-e1671005081868-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/NALA-team-photo-e1671005081868-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/NALA-team-photo-e1671005081868-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/startups/" class="article-list-category">startups</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/13/nala-expands-into-europe-to-enable-cross-border-payments/" class="article-list-title">
            NALA expands into Europe to enable cross border payments        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/muktar/" title="Posts by Muktar Oladunmade" rel="author">Muktar Oladunmade</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/12/13/founding-startups-in-africa/">
            <img width="240" height="160" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-240x160.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/12/dfghjkl-760x506.jpg 760w" loading="lazy" sizes="(max-width: 240px) 100vw, 240px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/startups/" class="article-list-category">startups</a>
                                            </div>
                        <a href="https://techcabal.com/2022/12/13/founding-startups-in-africa/" class="article-list-title">
            Founding startups in Africa        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/damilola-makinde/" title="Posts by Damilola Makinde" rel="author">Damilola Makinde</a></span>
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
                <div class="site-copyright-text">Copyright ©2023. All rights reserved. Privacy & Terms.</div>
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
print('Output === ')
print(data)