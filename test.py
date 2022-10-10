from app.tools.parser import Parser

input = '''

<!doctype html>
<html lang="en-US" class="no-js">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="pingback" href="https://techcabal.com/xmlrpc.php">
    
    <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO plugin v19.6.1 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>The leading African tech moves from September 2022 | TechCabal</title>
	<meta name="description" content="In September 2022, African tech startups announced raises totalling $383,465,000, the highest since June 2022. The funding was led by Bboxx’s $200 million acquisition of PEG Africa." />
	<link rel="canonical" href="https://techcabal.com/2022/10/03/leading-tech-moves-september/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="The leading African tech moves from September 2022 | TechCabal" />
	<meta property="og:description" content="In September 2022, African tech startups announced raises totalling $383,465,000, the highest since June 2022. The funding was led by Bboxx’s $200 million acquisition of PEG Africa." />
	<meta property="og:url" content="https://techcabal.com/2022/10/03/leading-tech-moves-september/" />
	<meta property="og:site_name" content="TechCabal" />
	<meta property="article:publisher" content="https://www.facebook.com/TechCabal" />
	<meta property="article:published_time" content="2022-10-03T05:30:00+00:00" />
	<meta property="article:modified_time" content="2022-10-05T11:20:33+00:00" />
	<meta property="og:image" content="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/May-2022-3.png" />
	<meta property="og:image:width" content="1920" />
	<meta property="og:image:height" content="1080" />
	<meta property="og:image:type" content="image/png" />
	<meta name="author" content="Timi Odueso" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@timiodueso" />
	<meta name="twitter:site" content="@techcabal" />
	<meta name="twitter:label1" content="Written by" />
	<meta name="twitter:data1" content="Timi Odueso" />
	<meta name="twitter:label2" content="Est. reading time" />
	<meta name="twitter:data2" content="10 minutes" />
	<!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Feed" href="https://techcabal.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; Comments Feed" href="https://techcabal.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="TechCabal &raquo; The leading African tech moves from September 2022 Comments Feed" href="https://techcabal.com/2022/10/03/leading-tech-moves-september/feed/" />
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
<link rel='stylesheet' id='parent-style-css'  href='//x7d4c5z5.stackpathcdn.com/wp-content/themes/bcm/style.css?ver=7.0.0.5' type='text/css' media='all' />
<link rel='stylesheet' id='child-style-css'  href='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/style.css?ver=7.0.0.5' type='text/css' media='all' />
<script type='application/json' id='wpp-json'>
{"sampling_active":0,"sampling_rate":100,"ajax_url":"https:\/\/techcabal.com\/wp-json\/wordpress-popular-posts\/v1\/popular-posts","api_url":"https:\/\/techcabal.com\/wp-json\/wordpress-popular-posts","ID":100689,"token":"000c73fb54","lang":0,"debug":0}
</script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/plugins/wordpress-popular-posts/assets/js/wpp.min.js?ver=6.0.5' id='wpp-js-js'></script>
<link rel="https://api.w.org/" href="https://techcabal.com/wp-json/" /><link rel="alternate" type="application/json" href="https://techcabal.com/wp-json/wp/v2/posts/100689" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://techcabal.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://techcabal.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 6.0.2" />
<link rel='shortlink' href='https://techcabal.com/?p=100689' />
<link rel="alternate" type="application/json+oembed" href="https://techcabal.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://techcabal.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F&#038;format=xml" />
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
                'author' : "Timi Odueso",
                'pagetitle' : "The leading African tech moves from September 2022",
                'publishdate' : "2022-10-03"
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

<body class="post-template-default single single-post postid-100689 single-format-standard  section-single"><div id="fb-root"></div>
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
    <div class="menu-wrapper"><ul class="menu"><li><a href="https://techcabal.com/tag/african-tech-roundup/">African tech roundup</a></li><li><a href="https://techcabal.com/tag/tc-daily/">TC Daily</a></li></ul></div></div>
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
<li id="menu-item-78282" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-has-children menu-item-78282"><a href="https://techcabal.com/category/newsletters/">Newsletters</a>
<ul class="sub-menu">
	<li id="menu-item-57883" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-57883"><a href="https://techcabal.com/category/newsletters/tc-daily/">TC Daily</a></li>
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
<script type='application/ld+json'>{"@context":"https:\/\/schema.org\/","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/techcabal.com\/2022\/10\/03\/leading-tech-moves-september\/"},"headline":"The leading African tech moves from September 2022","image":["https:\/\/x7d4c5z5.stackpathcdn.com\/wp-content\/uploads\/tc\/2022\/10\/May-2022-3.png"],"datePublished":"2022-10-03T06:30:00+01:00","dateModified":"2022-10-05T12:20:33+01:00","author":{"@type":"Person","name":"Timi Odueso"},"publisher":{"@type":"Organization","url":"https:\/\/techcabal.com","name":"TechCabal","logo":"https:\/\/x7d4c5z5.stackpathcdn.com\/wp-content\/themes\/tc1.5\/images\/tclogo-desktop.png"}}</script><section class="single-article">
    <div class="content">
        <article>
            <div class="single-article-meta">
                <div class="single-article-category">
                    <a href="https://techcabal.com/category/newsletters/">Newsletters</a>
                </div>
                <h1 class="single-article-title">
                    The leading African tech moves from September 2022                </h1>
                <div class="single-article-info">
                    <span class="single-article-author">
                        <a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a>                    </span>
                    <span class="single-article-date">3rd October 2022</span>
                </div>
            </div>
            <div class="single-article-main tc-daily-single">
                <div class="single-article-content" id="single-article">
                    
<div class="tc-daily-wrapper" style="background-color: #f5f5f5; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; font-size: 16px; line-height: 1.5; text-rendering: optimizeLegibility !important; -webkit-font-smoothing: antialiased !important; color: #373736; width: 100%; max-width: 550px; margin: 0 auto; padding: 10px; box-sizing:border-box;">
    <div id="intro" class="content_cont" style="background-color: #ffffff;padding: 40px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;text-align: center;border-bottom: 5px solid #f23204;">
        <div id="tc_n_logo" style="margin-bottom: 30px;">
            <img style="width: 45%; height: auto;" 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520842.png" alt="TC Daily Logo">
        </div>
        <div id="tc_n_date" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; font-size: 20px;margin-bottom: 20px;">
            <span style="display: inline-block;padding: 0 10px;border-left: 2px solid #F23204;border-right: 2px solid #F23204;line-height">3 OCTOBER, 2022
            </span>
        </div>

        <div id="tc_n_partnership" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; margin-bottom:30px">
            <h2 style="font-size: 17px;margin-bottom:5px">IN PARTNERSHIP WITH</h2>
            <div style="color: #373736;">
                <img style="width: auto; height: 35px;position:relative;vertical-align: middle;margin-right: 10px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/03/Untitled-design-12-e1646335829132.png" alt="Flutterwave Logo">




            </div>
        </div>

        <div id="tc_intro_content" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; font-size: 16px;">
            <div class="tc_intro_text" style="max-width: 425px;margin: 0 auto;color: #373736;">
                <p style="margin: 20px 0;">
                    <strong>

                    Happy new month 🚀
                    </strong>
                </p>
<p>This month started off on a sour note with news of yet another coup d’etat in Burkina Faso.&nbsp;</p>
<p>Eight months after Lt-Col Paul-Henri <a href="https://www.theguardian.com/world/2022/jan/24/burkina-faso-government-denies-coup-after-army-mutiny-and-gunfire-near-presidents-home" style="color: #14a673; font-weight: 700;">Damiba overthrew</a> the democratically-elected Burkinabe government and installed himself as (military) president of Burkina Faso, yet another army official has overthrown Damiba.&nbsp;</p>
<p>Last Friday, army captain Ibrahim Traore led a coup and announced on national television that the <a href="https://www.bbc.com/news/world-africa-60118993" style="color: #14a673; font-weight: 700;">army had seized power</a> and ousted military leader Paul Henri Damiba.</p>
<p>Counting the alleged attempted coup in Mali, this is the third coup in Africa this year.</p>

            <div style="text-align: left;margin-top: 20px;color: #373736;">

               <p>
                        <strong> In today&#8217;s edition</strong>
                    </p>
                    <ul>
                        <li><a href="#Crypto" style="color: #000000; font-weight: 700;">Crypto market</a></li>
                        <li><a href="#Story1" style="color: #000000; font-weight: 700;">The leading tech moves from September </a></li>
                        <li><a href="#Story2" style="color: #000000; font-weight: 700;">TC Insights: A new era</a></li>
                        <li><a href="#Game" style="color: #000000; font-weight: 700;">Game: Unscramble &#8220;Nigerian&#8221;</a></li>
                        <li><a href="#Opportunities" style="color: #000000; font-weight: 700;">Job opportunities
 </a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>



   <div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">
        <h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010;" id="CryptoMarket"> CRYPTO MARKET</h2>

        <a href="https://techcabal.com/category/cryptocurrency/" style="text-decoration:none;">
            <table style="width: 100%;border-collapse:collapse;">
                <colgroup>
                    <col span="1" style="width: 33%;">
                    <col span="1" style="width: 33%;">
                    <col span="1" style="width: 33%;">
                </colgroup>
                <tbody><tr style="width: 100%;padding-bottom: 20px; border-bottom: 3px dotted #F23204;">
                    <th style="padding-bottom: 0px; padding-left: 10px;text-align: left;">
                        <img style="width:30px; height: auto; margin-left: 0;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/coins-vector.png">
                    </th>
                    <th>
                        <img style="width:35px; height: auto; margin-left: 0;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/price-vector.png">
                    </th>
                    <th>
                        <img style="width:30px; height: auto; margin-left: 0;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/tag-vector.png">
                    </th>
                </tr>
                </tbody><tbody>
                    <tr style="border-bottom: 3px dotted #fd9e8e;">
                        <td style="padding-bottom: 15px;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;">Bitcoin</p>
                            <img style="width: 20px; height: auto;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/red-arrow.png">
                        </td>
                        <td style="padding: 0;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;vertical-align: middle; text-align: center;">$19,278</p>
                        </td>
                        <td style="padding: 0;">
                            <p style="display: block; color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-weight: 600; vertical-align: middle; text-align: center;background-color: #fbc2b5; border-radius: 5px; width: 80px; height: 35px; line-height: 35px; box-shadow: 5px 5px #ef323d; margin-left: auto; margin-right: auto;">
                                &#8211; 0.16%</p>
                        </td>
                    </tr>
                  <tr style="border-bottom: 3px dotted #fd9e8e;">
                        <td style="padding-bottom: 15px;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;">Ether</p>
                            <img style="width: 20px; height: auto;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/red-arrow.png">
                        </td>
                        <td style="padding: 0;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;vertical-align: middle; text-align: center;">$1,304</p>
                        </td>
                        <td style="padding: 0;">
                            <p style="display: block; color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-weight: 600; vertical-align: middle; text-align: center;background-color: #fbc2b5; border-radius: 5px; width: 80px; height: 35px; line-height: 35px; box-shadow: 5px 5px #ef323d; margin-left: auto; margin-right: auto;">
                                &#8211; 0.87%</p>
                        </td>
                    </tr>
                   <tr style="border-bottom: 3px dotted #fd9e8e;">
                        <td style="padding-bottom: 15px;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;">BNB</p>
                            <img style="width: 20px; height: auto;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/green-arrow.png">
                        </td>
                        <td style="padding: 0;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;vertical-align: middle; text-align: center;">$286</p>
                        </td>
                        <td style="padding: 0;">
                            <p style="display: block; color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-weight: 600; vertical-align: middle; text-align: center;background-color: #7ed957; border-radius: 5px; width: 80px; height: 35px; line-height: 35px; box-shadow: 5px 5px #008037; margin-left: auto; margin-right: auto;">
                                + 1.09%</p>
                        </td>
                    </tr>
                    <tr style="border-bottom: 3px dotted #fd9e8e;">
                        <td style="padding-bottom: 15px;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;">Solana</p>
                            <img style="width: 20px; height: auto;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/green-arrow.png">
                        </td>
                        <td style="padding: 0;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;vertical-align: middle; text-align: center;">$32.76</p>
                        </td>
                        <td style="padding: 0;">
                            <p style="display: block; color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-weight: 600; vertical-align: middle; text-align: center;background-color: #7ed957; border-radius: 5px; width: 80px; height: 35px; line-height: 35px; box-shadow: 5px 5px #008037; margin-left: auto; margin-right: auto;">
                                + 0.14%</p>
                        </td>
                    </tr>
                    <tr style="border-bottom: 3px dotted #fd9e8e;">
                        <td style="padding-bottom: 15px;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;">Cardano</p>
                            <img style="width: 20px; height: auto;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/red-arrow.png">
                        </td>
                        <td style="padding: 0;">
                            <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px;vertical-align: middle; text-align: center;">$0.42</p>
                        </td>
                        <td style="padding: 0;">
                            <p style="display: block; color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-weight: 600; vertical-align: middle; text-align: center;background-color: #fbc2b5; border-radius: 5px; width: 80px; height: 35px; line-height: 35px; box-shadow: 5px 5px #ef323d; margin-left: auto; margin-right: auto;">
                                &#8211; 0.93%
</p>
                        </td>
                    </tr>
                </tbody>
                <tbody><tr>
                    <td style="padding-bottom: 0px;" colspan="2">
                        <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-style: italic; vertical-align: middle;">
                            <img style="width: 18px; height: auto; margin-right: 5px; vertical-align: text-bottom;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/coins-vector.png">
                            Name of the coin
                        </p>
                        <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-style: italic; vertical-align: middle;">
                            <img style="width: 18px; height: auto; margin-right: 5px; vertical-align: text-bottom;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/price-vector.png">
                            Price of the coin
                        </p>
                        <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-style: italic; vertical-align: middle;">
                            <img style="width: 18px; height: auto; margin-right: 5px; vertical-align: text-bottom;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/tag-vector.png">
                            24-hour percentage change
                        </p>
                    </td>
                    <td style="padding-bottom: 0px;" colspan="1">
                        <h5 style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; vertical-align: middle;">
                            Source:
                            <span style="font-size: 16px;font-weight: normal;display: block;">CoinMarketCap</span>
                        </h5>
                        <p style="color:#000000; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 14px; font-style: italic; vertical-align: middle;">
                            <img style="width: 100px; height: auto; margin-right: 5px; vertical-align: text-bottom;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/tc-logo-orange.png">
                        </p>
                    </td>
                </tr>
            </tbody></table>
        </a>
        <p style="margin: 20px 0;">
            <em>* Data as of 20:30  PM WAT, October 3, 2022.</em>
        </p>

  <br>
<a href="https://api.whatsapp.com/send?text=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Whatsapp-Icon.png" border="0" alt="WhatsApp"></a>
<a href="https://twitter.com/intent/tweet?url=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Twitter-icon-1.png" border="0" alt="Twitter"></a>
<a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://techcabal.com/2022/10/03/leading-tech-moves-september/;summary=&amp;source=" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/LinkedIn-Icon-1.png" border="0" alt="LinkedIn"></a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Facebook-icon-1.png" border="0" alt="Facebook"></a>
<a href="mailto:info@example.com?&amp;subject=&amp;body=https://techcabal.com/2022/10/03/leading-tech-moves-september/?utm_source=Newsletter&amp;utm_medium=TC_daily" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Email-icon-1.png" border="0" alt="Email"></a>
</div>



<div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">

<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010;" id="Story1">THE LEADING TECH MOVES FROM SEPTEMBER
</h2>
<p>Since <a href="https://techcabal.com/2022/03/16/a-fantastic-february-for-african-tech-heres-what-matters/" style="color: #14a673; font-weight: 700;">February 2022</a>, we’ve reviewed the leading tech moves from countries across Africa.</p>
<p>While some months like <a href="https://techcabal.com/2022/07/05/the-biggest-african-tech-moves-from-june-2022/" style="color: #14a673; font-weight: 700;">June</a> are filled with news of tech layoffs, others like <a href="https://techcabal.com/2022/08/05/the-leading-tech-moves-from-july/" style="color: #14a673; font-weight: 700;">July</a> come with fraud allegations.</p>
<p>September was, by all accounts, a chill month. So what were the leading tech moves announced in it?</p>
<p>Let’s find out!</p>
<a href="https://techcabal.com/2022/09/05/leading-tech-moves-august/">
<img style="margin: 20px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/May-2022-3.png"></a>

<div class="divider" style=" height: 3px; background-color: #F23204;"></div>

<p><strong>1. FUNDING: ENERGY TAKES THE LEAD
</strong></p>
<p>In September 2022, African startups made 36 fully disclosed* raises totalling $383,465,000. So far, this total is the highest amount raised in a month by African startups since June 2022, a 75.9 % increase from <a href="https://techcabal.com/2022/09/05/leading-tech-moves-august/" style="color: #14a673; font-weight: 700;">August’s $218,000,000</a>. This month’s raise was led by Bboxx’s $200 million acquisition of PEG Africa.</p>
<p><strong>Per sector</strong>, the top three sectors in September are energy, fintech and e-commerce. Energy startups raised $201,000,000 (52.4%), fintech startups raised $87,945,000 (22.9%), and e-commerce/retail startups raised $35,550,000 (9.3%).</p>
<a href="https://techcabal.com/2022/09/05/leading-tech-moves-august/">
<img style="margin: 20px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Funding-Analysis-2.png"></a>
<p><strong>Per region</strong>, West Africa led with $313,045,000 of the funding. Next is East Africa with $27,220,000, while South African startups came a close third with $26,650,000. North Africa brought in the lowest funding from September with $16,650,000 in disclosed funding.&nbsp;</p>
<a href="https://techcabal.com/2022/09/05/leading-tech-moves-august/">
<img style="margin: 20px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Funding-Analysis-3.png"></a>
<p>The top five disclosed deals of September 2022 are</p>
<ol>
<li>Bboxx’s $200 million acquisition of Ghana-based cleantech PEG Africa.</li>
<li>Nigerian crypto exchange startup Yellowcard’s <a href="https://techcabal.com/2022/09/19/yellow-card-40-million-series-b/" style="color: #14a673; font-weight: 700;">$40 million Series B raise</a>.</li>
<li>Nigerian digital procurement platform Vendease’s <a href="https://techcabal.com/2022/09/26/vendease-raises-30-million-to-offer-procurement-services-across-africa/" style="color: #14a673; font-weight: 700;">$30 million raise</a>.</li>
<li>South African biometrics platform iiDENTIFii’s <a href="https://techcabal.com/2022/09/28/iidentifii-15-million/" style="color: #14a673; font-weight: 700;">$15 million raise</a>.</li>
<li>Nigerian fintech NowNow’s <a href="https://techcabal.com/2022/09/07/nownow-raises-13-million-in-seed-funding-to-expand-services-across-africa/" style="color: #14a673; font-weight: 700;">$13 million seed round</a>.</li>
</ol>
<p><em>Note: This data compiles only funding deals announced in September 2022. Raises are often announced later than when the deals are actually made.&nbsp;</em></p>
<p><em>This data is exclusive of estimated grants from accelerators like Techstars or Y Combinator.</em></p>
<br>
<a href="https://api.whatsapp.com/send?text=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Whatsapp-Icon.png" border="0" alt="WhatsApp"></a>
<a href="https://twitter.com/intent/tweet?url=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Twitter-icon-1.png" border="0" alt="Twitter"></a>
<a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://techcabal.com/2022/10/03/leading-tech-moves-september/;summary=&amp;source=" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/LinkedIn-Icon-1.png" border="0" alt="LinkedIn"></a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Facebook-icon-1.png" border="0" alt="Facebook"></a>
<a href="mailto:info@example.com?&amp;subject=&amp;body=https://techcabal.com/2022/10/03/leading-tech-moves-september/?utm_source=Newsletter&amp;utm_medium=TC_daily" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Email-icon-1.png" border="0" alt="Email"></a>
</div>


<div class="content_cont tc_quiz" style="background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">
<div class="tc_category" style="color: #F23204;font-weight: 700;margin: 10px 0 20px;">
SEND BY FLUTTERWAVE
</div>
<figure style="margin: 20px 0 30px; text-align: right;">
<p style="margin: 20px 0;">
<a href="http://send.flutterwave.com/">
<img style="width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/03/Send.jpg"> </a>
</p>
</figure>
<div class="tc_text" style="color: #373736;">
<p style="margin: 20px 0;">
Don&#8217;t just send money, send money fast. Send and receive money directly to mobile wallets, bank accounts, Barter or through cash pickup with $end.
</p>
<p style="margin: 20px 0;">
Visit <a href="http://send.flutterwave.com/" style="color: #14a673; font-weight: 700;">send.flutterwave.com</a> and do it now!
</p>
<p style="margin: 20px 0;color: #F23204">
<em>This is partner content.</em>
</p>

</div>
</div>



<div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">

<p><strong>2. LAGOS SUSPENDED ITS TECH HUB AUDITS</strong></p>
<p>The Lagos State Safety Commission (LASG Safety) in Nigeria guarded its words carefully in September.</p>
<p>First, LASG Safety <a href="https://techcabal.com/2022/09/28/techcabal-daily-lagos-bills-tech-hubs/?utm_source=dlvr.it&amp;utm_medium=twitter" style="color: #14a673; font-weight: 700;">planned annual safety audits</a> that would cost tech hubs and co-working spaces in Lagos ₦150,000 ($347) per year.</p>
<p>The news of the fees was received with negative feedback on and offline, and the Commission promptly announced that it would <a href="https://techcabal.com/2022/09/28/lagos-safety-commission-suspends-tech-hub-audits/" style="color: #14a673; font-weight: 700;">suspend the safety audits</a> and, instead, work to train stakeholders.</p>

<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong>3. UBER FACED REGULATORY HURDLES IN KENYA</strong></p>
<p>Months after similar regulatory hurdles forced it to exit in Tanzania, September saw Uber fighting in Kenya.</p>
<p>Kenya’s National Transport and Safety Authority (NTSA) planned to enforce <a href="https://techcabal.com/2022/09/14/after-exiting-tanzania-uber-is-struggling-to-remain-in-kenya-amidst-commission-wars/" style="color: #14a673; font-weight: 700;">a regulation</a> that caps commission for all ride-hailing companies in the country at 18%. Uber is <a href="https://www.google.com/amp/s/techcrunch.com/2022/09/08/uber-wants-court-to-nullify-kenyas-new-ride-hailing-law-that-caps-service-fee-at-18/amp/" style="color: #14a673; font-weight: 700;">appealing</a> to the Supreme Court to nullify the regulation.</p>
<p>Uber might be for the legislation but its drivers are not. In September, ride-hailing drivers staged <a href="https://techcabal.com/2022/09/27/uber-and-bolt-drivers-stage-go-slow-protest-in-kenya/" style="color: #14a673; font-weight: 700;">another protest</a> against high commission fees in Kenya.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>4. SAFARICOM ANNOUNCED ITS PLANNED SEPARATION FROM M-PESA</strong></strong></p>
<p>In September, telco Safaricom announced that it would be <a href="https://techcabal.com/2022/09/27/safaricoms-separation/" style="color: #14a673; font-weight: 700;">splitting</a> from its mobile money service M-Pesa by January 2023.</p>
<p>The <a href="http://www.parliament.go.ke/sites/default/files/2019-10/Kenya%20Information%20and%20Communication%20%28Amendment%29%20Bill%2C%202019-No.2_compressed.pdf" style="color: #14a673; font-weight: 700;">announcement</a> comes two years after the enactment of Kenya’s Information and Communications (Amendment) Bill, which sought to split all telcos from their mobile money businesses.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>5. CBK LICENSED 10 DIGITAL LENDERS</strong></strong></p>
<p>In September, the <a href="https://techcabal.com/2022/09/15/techcabal-daily-cbk-v-digital-lenders/" style="color: #14a673; font-weight: 700;">6-month ultimatum</a> the Central Bank of Kenya (CBK) gave for all digital lenders to apply for operational licences lapsed.&nbsp;</p>
<p>Only <a href="https://techcabal.com/2022/09/19/central-bank-of-kenya-licenses-only-10-digital-lenders/#:~:text=These%20are%20CeresTech%20Limited%2C%20Getcash,Innovation%20Limited%20and%20Sokohela%20Limited." style="color: #14a673; font-weight: 700;">10 digital lenders</a>, although the CBK did note that it received over 228 applications and is still reviewing many other applications.</p>

<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>6. CELLULANT AND ORANGE PARTNERED WITH 8 BATSWANA BANKS</strong></strong></p>
<p>Last month, Orange Money, the mobile money service of Orange and pan-African payments company, Cellulant, <a href="https://techcabal.com/2022/09/13/cellulant-partners-with-orange-money-botswana/" style="color: #14a673; font-weight: 700;">launched a partnership</a> to enable card-to-wallet transfers for 8 banks in Botswana.</p>
<p>The partnership will enable customers to transfer money online from any bank account to an Orange Money wallet, even if they don’t have Orange Money accounts.</p>

<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong>7. SIXTY AFRICAN STARTUPS RECEIVED $4 MILLION FROM GOOGLE </strong></p>

<p>September also saw <a href="https://techcabal.com/2022/09/06/60-african-startups-4-million-equity-funding-google/" style="color: #14a673; font-weight: 700;">60 African startups</a> receiving equity-free funding from Google.</p>
<p>As part of Google for Startups Black Founders Fund, startups like Eversend, Zuberi and Norebase will be part of a 6-month training programme and receive equity-free funding between $50,000 and $100,000.</p>
</div>


<div class="content_cont" style="background-color: #ffffff;padding: 5px 20px;border: 1px solid #f23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">
<div class="tc_category" style="color: #f23204;font-weight: 700;margin: 10px 0 20px;">
SELL MORE WITH PAYSTACK
</div>
<figure style="margin: 20px 0 30px; text-align: right;">
<p style="margin: 20px 0;">
<a href="http://paystack.com/storefront">
<img style="margin: 5px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/07/Paystack.png" alt="Paystack"> </a>
</p>
</figure>
<div class="tc_text" style="color: #373736;">
<p>Increase your online sales with a Paystack Storefront &#8211; a free, beautiful seller page that helps you bring creative ideas to life.</p>
<p>👉🏾 Learn more at <a href="http://paystack.com/storefront" style="color: #14a673; font-weight: 700;">paystack.com/storefront</a>.</p>
<p style="margin: 20px 0;color: #f23204">
<em>This is partner content.</em>
</p>
</div>
</div>

<div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">


<p><strong><strong>8. OVER 2,000 NIGERIAN INVESTORS SUED IN KENYA</strong></strong></p>

<p>In relation to the $59.2 million <a href="https://techcabal.com/2022/07/07/kenya-freezes-flutterwaves-accounts/" style="color: #14a673; font-weight: 700;">frozen</a> by Kenya’s Asset Recovery Agency (ARA) in fraud investigations levied against Nigerian startups in Kenya, over 2,000 Nigerian investors have <a href="https://techcabal.com/2022/09/26/techcabal-daily-nigerian-investors-sue-in-kenya/" style="color: #14a673; font-weight: 700;">petitioned courts in Kenya</a> to have their monies unfrozen.</p>
<p>The 2,468 Nigerian investors claim they were swindled to the tune of Ksh 1.44 billion ($11 million) by a dubious person via transactions on Flutterwave, one of the startups being investigated by the ARA. The investors now want their money unfrozen.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>9. FREE TRANSFERS IN TANZANIA</strong></strong></p>
<p>Last month, the Tanzanian government <a href="https://techcabal.com/2022/09/22/techcabal-daily-transfer-fees-tanzanians/#Story3" style="color: #14a673; font-weight: 700;">announced its new plan</a> to encourage more people to use mobile money.</p>
<p>Starting in October, Tanzanians will no longer have to pay transfer fees on withdrawal of cash through bank agents and ATMs for Tsh30,000 ($12.81) and below.&nbsp;</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>10. SHELL ACQUIRED DAYSTAR</strong></strong></p>

<p>After three years of negotiation, global oil giant, Shell, <a href="https://techcabal.com/2022/09/29/why-west-african-solar-company-daystar-power-is-selling-to-oil-major-shell/" style="color: #14a673; font-weight: 700;">acquired Daystar Power</a>, a West African solar power company for an undisclosed amount of money in September.</p>
<p>The acquisition has been in the works since 2019 and Daystar Power caved in due to the rising demand for its services.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>11. EBANX EXPANDED INTO AFRICA</strong></strong></p>
<p>Last month also saw multinational fintech company EBANX announce <a href="https://techcabal.com/2022/09/14/brazilian-unicorn-ebanx-expands-into-africa/" style="color: #14a673; font-weight: 700;">plans to expand into Africa</a> with a focus on Kenya, Nigeria and South Africa.</p>
<p>In South Africa, the fintech plans to implement internet banking solutions while its foray into Nigeria and Kenya will see it offering mobile money and USSD services.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>12. UGANDA PASSED THE COMPUTER MISUSE BILL</strong></strong></p>
<p>On the tech regulations side, the Ugandan parliament in September <a href="https://techcabal.com/2022/09/09/uganda-computer-bill/" style="color: #14a673; font-weight: 700;">passed</a> the Computer Misuse (Amendment) Bill, 2022 which many critics believe will be used to suppress digital rights and free speech.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>13. NIGERIA CANCELED COMMUNICATIONS TAX</strong></strong></p>
<p>Last month, the Nigerian government also surprised people by <a href="https://techcabal.com/2022/09/07/techcabal-daily-nigeria-no-new-tax/" style="color: #14a673; font-weight: 700;">halting a new telecommunications tax</a> in its tracks.&nbsp;</p>
<p>The tax, a 5% levy, was supposed to go into effect this year but communications and digital economy minister, Isa Pantami, argued that the telecommunications sector is already overtaxed.</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>
<p><strong><strong>14. JUMIA PARTNERED WITH ZIPLINE FOR DRONE DELIVERY
</strong></strong></p>
<p>Jumia, Africa’s leading e-commerce player, <a href="https://techcabal.com/2022/09/26/jumia-signs-with-zipline-for-drone-delivery-services/" style="color: #14a673; font-weight: 700;">partnered with Zipline</a>, a global instant delivery company, to offer on-demand drone delivery services to the growing number of e-commerce players on the continent.&nbsp;</p>
<p>This launch comes after a pilot phase of this logistics service conducted in Ghana a few months ago.</p>
<br>
<p><em>Note: This list is in no particular order</em>.</p>
<br>
<a href="https://api.whatsapp.com/send?text=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Whatsapp-Icon.png" border="0" alt="WhatsApp"></a>
<a href="https://twitter.com/intent/tweet?url=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Twitter-icon-1.png" border="0" alt="Twitter"></a>
<a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://techcabal.com/2022/10/03/leading-tech-moves-september/;summary=&amp;source=" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/LinkedIn-Icon-1.png" border="0" alt="LinkedIn"></a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Facebook-icon-1.png" border="0" alt="Facebook"></a>
<a href="mailto:info@example.com?&amp;subject=&amp;body=https://techcabal.com/2022/10/03/leading-tech-moves-september/?utm_source=Newsletter&amp;utm_medium=TC_daily" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Email-icon-1.png" border="0" alt="Email"></a>
</div>




<div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">

<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010;" id="Story2">TC INSIGHTS: A NEW ERA
</h2>
<p>Across the globe, the financial services industry is faced with competition from fintech startups. They leverage technology to increase access to financial services to previously underbanked and unbanked segments of the population. Nigeria is no exception to this rule. Buoyed by the successful <a href="https://techcabal.com/2020/10/15/stripe-acquires-paystack/" style="color: #14a673; font-weight: 700;">acquisition</a> of local startup Paystack by payment giant Stripe in 2020, fintech startups in the country received over <a href="https://guardian.ng/news/fintech-operators-account-for-63-funding-raised-in-2021-association/#:~:text=Fintech.,raised%20in%20Nigeria%20in%202021." style="color: #14a673; font-weight: 700;">60%</a> of the $1.3 billion raised by Nigerian startups last year.&nbsp;</p>
<p>The success achieved by these startups lies a great deal in the path created by commercial banks in the country in the last two decades.&nbsp;</p>
<p>“Nigerian banks were the incubators or early supporters of Fintechs in Nigeria. For example, Flutterwave grew out of Access Bank. Teamapt grew out of Fidelity Bank and Wema Bank. Paystack&#8217;s connection with banks was critical for early success,” Adedeji Olowe, founder of Lendsqr and a Trustee of Open Banking Nigeria, shared in a text with TechCabal</p>
<p>Unsatisfied by the background role, commercial banks have floated fintech verticals to rival the existing fintech startups. Hydrogen, Squad, Alat, and PaywithSpecta are fintech products fromAccess Bank, GT Holdings, Wema Bank and Sterling Bank respectively.</p>

<img style="margin: 20px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Playground.png">
<p>In 2020, Nigeria’s top five banks, commonly known as FUGAZ made <a href="https://www.statista.com/statistics/1319620/leading-banks-in-nigeria-by-total-profit/" style="color: #14a673; font-weight: 700;">$1.56 billion</a> in profits, a huge disparity compared to some fintechs who operate at a loss despite their sky-high valuations. Yet, a huge financial war chest doesn’t always equate to market dominance in unfamiliar terrain.&nbsp;</p>
<p>“Frankly, the banks have no chance of success. They would pump money into these fintechs and most of them would fail abysmally. Banks would run the fintechs like a bank; slow and full of red tape. Nothing would move fast. Customer experience and support would be poor. Merchants and other users who are used to a better experience with fintechs wouldn&#8217;t care. Banks would not be able to attract the type of talent that can make things happen. Smart talents are scared of banks,” Olowe further shared</p>
<p>As opposed to competing with fintechs, banks could partner with them to maximise their comparative advantages and achieve their objectives. Yet the result of previous partnerships serves as a cautionary tale. The difference in organisational outlook and structures reduces the success of these partnerships.“Banks and the fintechs don&#8217;t have the same DNA, the difference which can be papered over with simple partnerships but which would be disastrous with a closer tie-in required for the type of partnerships that banks want. For example, fintechs are lax with processes and governance while banks are slow, plodding, and bureaucratic,” Olowe concluded.</p>
<p>It’s still a bit early to predict the outcome of banks&#8217; foray into the fintech space but the status quo is unlikely to face any form of disruption. Although, more partnerships between banks and better-governed fintechs will spring up in the coming years.</p>
<br>
<a href="https://api.whatsapp.com/send?text=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Whatsapp-Icon.png" border="0" alt="WhatsApp"></a>
<a href="https://twitter.com/intent/tweet?url=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Twitter-icon-1.png" border="0" alt="Twitter"></a>
<a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://techcabal.com/2022/10/03/leading-tech-moves-september/;summary=&amp;source=" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/LinkedIn-Icon-1.png" border="0" alt="LinkedIn"></a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Facebook-icon-1.png" border="0" alt="Facebook"></a>
<a href="mailto:info@example.com?&amp;subject=&amp;body=https://techcabal.com/2022/10/03/leading-tech-moves-september/?utm_source=Newsletter&amp;utm_medium=TC_daily" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Email-icon-1.png" border="0" alt="Email"></a>
</div>

<div class="content_cont" style="background-color: #ffffff;padding: 5px 20px;border: 1px solid #f23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">
<div class="tc_category" style="color: #f23204;font-weight: 700;margin: 10px 0 20px;">
APPLY FOR THE YOUTHADAPT CHALLENGE
</div>
<figure style="margin: 20px 0 30px; text-align: right;">
<p style="margin: 20px 0;">
<a href="http://www.youthadapt.africa">
<img style="margin: 5px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/YouthAdapt-SM-gca_600x400-1.jpg" alt="Paystack"> </a>
</p>
</figure>
<div class="tc_text" style="color: #373736;">
<p>The 2022 YouthADAPT Challenge is open for entries. The Global Center on Adaptation (GCA) and the African Development Bank (AfDB) are awarding $100,000 grants each to 20 enterprises that offer climate change adaptation solutions in Africa.&nbsp;</p>
<p><a href="http://www.youthadapt.africa" style="color: #14a673; font-weight: 700;">Apply before October 4</a>.</p>
<p style="margin: 20px 0;color: #f23204">
<em>This is partner content.</em>
</p>
</div>
</div>

<div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">

<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010;" id="Story2">GAME: UNSCRAMBLE &#8220;NIGEERIAN&#8221;
</h2>
<a href="https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/">
<img style="margin: 20px 0; width: 100%; height: auto; border-radius: 7px;" 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/09/Artboard-1-copy-13.jpg"></a>
<p>Nigeria turned 62 last week! Celebrate Nigerians for 10 minutes by <a href="https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/" style="color: #14a673; font-weight: 700;">playing this game</a>.&nbsp;</p>
<br>
<a href="https://api.whatsapp.com/send?text=https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Whatsapp-Icon.png" border="0" alt="WhatsApp"></a>
<a href="https://twitter.com/intent/tweet?url=https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Twitter-icon-1.png" border="0" alt="Twitter"></a>
<a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/;summary=&amp;source=" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/LinkedIn-Icon-1.png" border="0" alt="LinkedIn"></a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Facebook-icon-1.png" border="0" alt="Facebook"></a>
<a href="mailto:info@example.com?&amp;subject=&amp;body=https://techcabal.com/2022/10/01/tc-game-unscramble-nigerian/?utm_source=Newsletter&amp;utm_medium=TC_daily" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/05/Email-icon-1.png" border="0" alt="Email"></a>
</div>


<div class="content_cont" style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Ubuntu, 'Helvetica Neue', Oxygen, Cantarell, sans-serif; background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">



<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010;">
IN OTHER NEWS FROM TECHCABAL

</h2>
Rain submits <a href="https://techcabal.com/2022/10/01/rain-telkom-merger-proposal/" style="color: #14a673; font-weight: 700;">formal merger proposal</a> to Telekom board.<p></p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>

<p>Investors require startups to have <a href="https://techcabal.com/2022/09/30/yc-requires-startups-to-have-technical-co-founders-but-is-that-necessary/" style="color: #14a673; font-weight: 700;">technical co-founders</a>. But is that necessary?</p>
<div class="divider" style=" height: 3px; background-color: #F23204;"></div>

<p>Have Nigerians found a <a href="https://techcabal.com/2022/09/30/picoin-in-nigeria/" style="color: #14a673; font-weight: 700;">new crypto heaven or hell in PiCoin</a>?</p>

</div>













<div class="content_cont" style="background-color: #ffffff;padding:5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">
<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010;" id="Opportunities">JOB OPPORTUNITIES
</h2>
<ul>
<li><strong>TechCabal </strong>&#8211; <a href="https://theorg.com/org/big-cabal-media/jobs/news-editor-techcabal-e0ce9591" style="color: #14a673; font-weight: 700;">News Editor</a> &#8211; Africa (Remote)</li>
</ul>
<ul>
<li><strong>Healthforce </strong>&#8211; <a href="https://healthforcepeopleops.bamboohr.com/jobs/view.php?id=25" style="color: #14a673; font-weight: 700;">Product Designer (UI/UX) </a>&#8211; South Africa</li>
</ul>
<ul>
<li><strong>Tek Experts </strong>&#8211; <a href="https://careers-tekexperts.icims.com/jobs/9051/senior-ui-ux-designer/job?mode=viewhttps%3A%2F%2Fcareers-tekexperts.icims.com%2Fjobs%2F8956%2Fsenior-data-scientist%2Fjob%3Fmode%3Dvie&amp;iis=Job+Board&amp;iisn=LinkedIn" style="color: #14a673; font-weight: 700;">Senior UI/UX Designer</a> &#8211; Lagos, Nigeria</li>
</ul>
<ul>
<li><strong>GitLab</strong> &#8211; <a href="https://boards.greenhouse.io/gitlab/jobs/6364004002?lever-origin=applied&amp;lever-source=LINKEDIN" style="color: #14a673; font-weight: 700;">Product Designer</a> &#8211; South Africa (Remote)</li>
</ul>
<ul>
<li><strong>Tangent</strong> &#8211; <a href="https://tangentpeople.bamboohr.com/careers/31?source=aWQ9OQ%3D%3D" style="color: #14a673; font-weight: 700;">Senior Product Designer </a>&#8211; South Africa (Remote)</li>
</ul>
<ul>
<li><strong>Digitise &#8211;</strong><a href="https://jobs.gohire.io/digitise-xwcfqaab/ux-ui-web-designer-105843/?source=linkedin" style="color: #14a673; font-weight: 700;">UI/UX Web Designer</a> &#8211; Kenya, Zimbabwe</li>
</ul>
<ul>
<li><strong>MultiGate </strong>&#8211; <a href="https://www.linkedin.com/jobs/view/3281511062" style="color: #14a673; font-weight: 700;">Product Designer</a> &#8211; Lagos, Nigeria</li>
</ul>
<p>There are more jobs on <a href="https://techcabal.com/jobs/" style="color: #14a673; font-weight: 700;">TechCabal’s job board</a>. If you have job opportunities to share, submit them at <a href="http://bit.ly/tcxjobs" style="color: #14a673; font-weight: 700;">bit.ly/tcxjobs</a>.&nbsp;</p>
</div>




<div class="content_cont" style="background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f23204;">
<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #101010; text-transform: uppercase;">
What else is happening in tech?
</h2>
<figure style="margin: 20px 0 30px; text-align: justify;">
<ul>
<li><a href="https://www.benjamindada.com/nigerian-tech-entrepreneurs-national-awards/" style="color: #14a673; font-weight: 700;">Four Nigerian tech entrepreneurs</a> to receive the highest national awards.</li>
</ul>
<ul>
<li>Binance launches programme to <a href="https://ventureburn.com/2022/10/binance-launches-programme-to-combat-crypto-crimes/" style="color: #14a673; font-weight: 700;">combat crypto crimes</a>.</li>
</ul>
<ul>
<li>Absa Bank Kenya <a href="https://www.itnewsafrica.com/2022/09/absa-bank-kenya-partners-with-huawei-to-accelerate-digital-transformation/" style="color: #14a673; font-weight: 700;">partners with Huawei</a> to accelerate digital transformation.</li>
</ul>
<ul>
<li>Tesla CEO <a href="https://www.theverge.com/2022/9/30/23374729/tesla-bot-ai-day-robot-elon-musk-prototype-optimus-humanoid" style="color: #14a673; font-weight: 700;">Elon Musk unveils prototype humanoid</a> Optimus robot.</li>
</ul>

</figure></div>



<div class="content_cont" style="background-color: #ffffff;padding: 5px 20px;border: 1px solid #F23204;border-radius: 7px;margin-bottom: 40px;border-bottom: 5px solid #f33204;">
<h2 class="tc_heading" style="font-weight: 800;line-height: 1.3;font-size: 1.4em;margin-bottom: 20px;color: #14a673; text-transform: uppercase;text-align: center;">
SHARE THIS NEWSLETTER</h2>
<ul style="list-style:none;padding:0;margin:0;margin-top: 10px;text-align: center;">
<li style="display:inline-block;margin:5px;"><a href="https://twitter.com/intent/tweet?url=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520520.png" style="width: auto; height: 25px;display:block;"></a></li>
<li style="display:inline-block;margin:5px;"><a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://techcabal.com/2022/10/03/leading-tech-moves-september/;summary=&amp;source=" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520516.png" style="width: auto; height: 25px;display:block;"></a></li>
<li style="display:inline-block;margin:5px;"><a href="https://api.whatsapp.com/send?text=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520521.png" style="width: auto; height: 25px;display:block;"></a></li>
<li style="display:inline-block;margin:5px;"><a href="https://www.facebook.com/sharer/sharer.php?u=https://techcabal.com/2022/10/03/leading-tech-moves-september/" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520515.png" style="width: auto; height: 25px;display:block;"></a></li>
<li style="display:inline-block;margin:5px;"><a href="mailto:info@example.com?&amp;subject=&amp;body=https://techcabal.com/2022/10/03/leading-tech-moves-september/?utm_source=Newsletter&amp;utm_medium=TC_daily" target="_blank" rel="noopener"><img 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520517.png" style="width: auto; height: 25px;display:block;"></a></li>
</ul>
</div>

<div class="content_cont_bare_child" style="text-align: center;border-bottom: 1px solid #F23204;">
<div class="halfed tc_tweet" style="max-width: 420px;margin: 50px auto;">
<p class="tc_tweeter" style="font-size: 15px;font-weight: 700;">

Written by &#8211; <a href="https://www.linkedin.com/in/timi-odueso/" style="color: #F23204; font-weight: 700;">Timi Odueso</a> &amp; <a href="https://www.linkedin.com/in/mob%E1%BB%8D%CC%81l%C3%A1j%C3%AD-ad%C3%A9b%C3%A1y%E1%BB%8D%CC%80/" style="color: #F23204; font-weight: 700;">Mobolaji Adebayo</a>
</p>
<p class="tc_tweeter" style="font-size: 15px;font-weight: 700;">
</p><p class="tc_tweeter" style="font-size: 15px;font-weight: 700;">
Edited by &#8211; <a href="https://www.linkedin.com/in/kelechi-njoku-5532118b/" style="color: #F23204; font-weight: 700;">Kelechi Njoku</a>
</p><p><strong>Want more of TechCabal?</strong> Sign up for our insightful newsletters on the business and economy of tech in Africa.&nbsp;</p>
<ul>
<li><strong><a href="https://techcabal.com/next-wave" style="color: #F23204; font-weight: 700;"></a></strong><a href="https://techcabal.com/next-wave" style="color: #F23204; font-weight: 700;">The Next Wave</a>: futuristic analysis of the business of tech in Africa.</li>
</ul>
<ul>
<li><a href="https://www.subscribepage.com/j9o7a9" style="color: #F23204; font-weight: 700;"><strong>TC Weekender</strong></a><strong> </strong>: weekly roundup of the most important tech news out of Africa.&nbsp;</li>
</ul>
<ul>
<li><a href="https://www.subscribepage.com/enteringtech" style="color: #F23204; font-weight: 700;"><strong>Entering Tech</strong></a><strong></strong>: tech career insights and opportunities in your inbox every Wednesday at 12 PM WAT.</li>
</ul>
<p></p>
<div class="halfed tc_ad_call" style="width: 300px;margin: 50px auto;font-size: 16px;">
<h3 class="tc_sub_heading" style="font-size: 15px;margin-bottom: 0;text-transform: uppercase;color: #000000;">
Advertise
</h3>
<p style="margin: 5px 0;color: #373736;">
To advertise with us, send an email to
</p>
<a href="ads@bigcabal.com" target="_blank" style="color: #14a673;font-weight: 700;" rel="noopener">ads@bigcabal.com</a>
</div>
<div class="halfed tc_footer_logo" style="width: 270px;margin: 50px auto;margin-bottom: 0;">
<img style="width: 130px;height: auto;" 
     	loading="lazy" src="https://images.benchmarkemail.com/client1281780/image9520843.png">
</div>
</div>
</div>
</div>
<div style="padding: 20px 0; text-align: center;">
<a style="font-size: 14px; text-decoration: none; color: #F23204;" href="{$unsubscribe}">Unsubscribe from TC Daily</a>
</div>



                    <div class="social-widget social-share">
                        <span>Share this article</span>
                        <ul class="social-links">
    <li><a target="_blank" href="https://twitter.com/share?url=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F&amp;text=The%20leading%20African%20tech%20moves%20from%20September%202022" class="share-icon share-twitter" data-type="twitter"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png" alt="Twitter" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/twitter_red@2x.png 2x"></a></li><li><a target="_blank" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F&amp;title=The%20leading%20African%20tech%20moves%20from%20September%202022&amp;summary=In%20September%202022%2C%20African%20tech%20startups%20announced%20raises%20totalling%20%24383%2C465%2C000%2C%20the%20highest%20since%20June%202022.%20%0A%0AThe%20funding%20was%20led%20by%20Bboxx%E2%80%99s%20%24200%20million%20acquisition%20of%20PEG%20Africa.%20%0A%0ARead%20more%20leading%20African%20tech%20moves%20from%20September%20in%20%23TCDaily.%20" class="share-icon share-linkedin" data-type="linkedin"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png" alt="Linkedin" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/linkedin_red@2x.png 2x"></a></li><li><a target="_blank" href="https://api.whatsapp.com/send?text=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F" class="share-icon share-whatsapp" data-type="whatsapp"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red.png" alt="WhatsApp" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/whatsapp_red@2x.png 2x"></a></li><li><a target="_blank" href="https://www.facebook.com/dialog/share?app_id=252296078952383&amp;display=popup&amp;href=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F" class="share-icon share-facebook" data-type="facebook"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png" alt="Facebook" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/facebook_red@2x.png 2x"></a></li><li><a target="_blank" href="mailto:?body=https%3A%2F%2Ftechcabal.com%2F2022%2F10%2F03%2Fleading-tech-moves-september%2F&amp;subject=The%20leading%20African%20tech%20moves%20from%20September%202022" class="share-icon share-email" data-type="email"><img src="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red.png" alt="Email" srcset="//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red.png 1x, //x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/images/mail_red@2x.png 2x"></a></li></ul>
                    </div>
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
        <a href="https://techcabal.com/2022/10/01/this-week-sky-garden-faces-shut-down/">
            <img width="800" height="450" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/The-Sky.Garden-founding-team-from-left-to-right-James-Mwai-Christian-Grubak-Isaac-Hunja-Martin-Majlund-Daniel-Maison-Morten-Grubak-2.jpg" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/The-Sky.Garden-founding-team-from-left-to-right-James-Mwai-Christian-Grubak-Isaac-Hunja-Martin-Majlund-Daniel-Maison-Morten-Grubak-2.jpg 800w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/The-Sky.Garden-founding-team-from-left-to-right-James-Mwai-Christian-Grubak-Isaac-Hunja-Martin-Majlund-Daniel-Maison-Morten-Grubak-2-300x169.jpg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/The-Sky.Garden-founding-team-from-left-to-right-James-Mwai-Christian-Grubak-Isaac-Hunja-Martin-Majlund-Daniel-Maison-Morten-Grubak-2-768x432.jpg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/The-Sky.Garden-founding-team-from-left-to-right-James-Mwai-Christian-Grubak-Isaac-Hunja-Martin-Majlund-Daniel-Maison-Morten-Grubak-2-690x388.jpg 690w" loading="lazy" sizes="(max-width: 800px) 100vw, 800px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/newsletters/" class="article-list-category">Newsletters</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/01/this-week-sky-garden-faces-shut-down/" class="article-list-title">
            This week: Sky.Garden faces shut down        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/ngozi/" title="Posts by Ngozi Chukwu" rel="author">Ngozi Chukwu</a></span>
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
        <a href="https://techcabal.com/2022/10/10/techcabal-daily-a-chella-lot/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Coachella-Valley-Music-Arts-Festival-Suing-Ghanas-Afrochella-Festival-Over-Copyright-Infringement-240x160.jpeg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Coachella-Valley-Music-Arts-Festival-Suing-Ghanas-Afrochella-Festival-Over-Copyright-Infringement-240x160.jpeg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Coachella-Valley-Music-Arts-Festival-Suing-Ghanas-Afrochella-Festival-Over-Copyright-Infringement-480x320.jpeg 480w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/newsletters/" class="article-list-category">Newsletters</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/10/techcabal-daily-a-chella-lot/" class="article-list-title">
            👨🏿‍🚀 TechCabal Daily &#8211; A Chella lot        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/10/08/this-week-nigeria-sues-meta/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/04/weekender-header-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/04/weekender-header-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/04/weekender-header-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/04/weekender-header-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/newsletters/" class="article-list-category">Newsletters</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/08/this-week-nigeria-sues-meta/" class="article-list-title">
            This Week: Nigeria sues Meta        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/10/07/techcabal-daily-pixel-perfect/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-300x200.jpg 300w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-768x512.jpg 768w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-690x460.jpg 690w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0-760x506.jpg 760w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Pixel_7_and_Pixel_7_Pro_Family.0.jpg 920w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/newsletters/" class="article-list-category">Newsletters</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/07/techcabal-daily-pixel-perfect/" class="article-list-title">
            👨🏿‍🚀TechCabal Daily &#8211; Pixel perfect        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/10/06/techcabal-daily-kenyas-audits/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Copy-of-Copy-of-TechCabals-Guide-to-Gift-Giving-2-1-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Copy-of-Copy-of-TechCabals-Guide-to-Gift-Giving-2-1-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Copy-of-Copy-of-TechCabals-Guide-to-Gift-Giving-2-1-480x320.jpg 480w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/newsletters/" class="article-list-category">Newsletters</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/06/techcabal-daily-kenyas-audits/" class="article-list-title">
            👨🏿‍🚀 TechCabal Daily &#8211; Kenya audits        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/10/05/enteringtech-five-soft-skills/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Five-no-code-tech-jobs-5-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="Five soft skills" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Five-no-code-tech-jobs-5-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Five-no-code-tech-jobs-5-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/Five-no-code-tech-jobs-5-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/consumer-tech/" class="article-list-category">Consumer Tech</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/05/enteringtech-five-soft-skills/" class="article-list-title">
            🚀EnteringTech #006: Five soft skills you need to learn        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>

<article class="article-list-item">
    <div class="article-list-img">
        <a href="https://techcabal.com/2022/10/05/techcabal-daily-one-charger/">
            <img width="195" height="130" src="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/USB-C-Over-Lightning-Feature-240x160.jpg" class="attachment-235x130 size-235x130 wp-post-image" alt="Image source: MacRumours" loading="lazy" srcset="https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/USB-C-Over-Lightning-Feature-240x160.jpg 240w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/USB-C-Over-Lightning-Feature-480x320.jpg 480w, https://x7d4c5z5.stackpathcdn.com/wp-content/uploads/tc/2022/10/USB-C-Over-Lightning-Feature-760x506.jpg 760w" loading="lazy" sizes="(max-width: 195px) 100vw, 195px" />        </a>
    </div>
    <div class="article-list-desc">
                            <div class="article-list-pretitle">
                        <a href="https://techcabal.com/category/newsletters/" class="article-list-category">Newsletters</a>
                                            </div>
                        <a href="https://techcabal.com/2022/10/05/techcabal-daily-one-charger/" class="article-list-title">
            👨🏿‍🚀TechCabal Daily &#8211; One charger to rule them all        </a>
                                <div class="article-list-meta">
                                                <span class="article-list-author"><a href="https://techcabal.com/author/timi/" title="Posts by Timi Odueso" rel="author">Timi Odueso</a></span>
                                                            </div>
                </div>
    
</article>
    </div>
                    </div>
                <div class="list-sidebar">
                    <div class="ad-box"><div class="ad" id="div-db-2"></div></div>                </div>
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
<template id="category-article-list-item">
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
</template>        <script>
            var googletag = googletag || {};
            googletag.cmd = googletag.cmd || [];

            googletag.cmd.push(function() {
                var sizemap = null;
                sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[970,90],[970,250],[728,90]]).addSize([ 300, 0 ], [[320,50],[300,100],[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc-homepage-top-leaderboard', [[970,90],[970,250],[728,90],[320,50],[300,100],[300,250]], 'div-db-0').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_300_new_2', [[300,250],[300,250]], 'div-db-1').defineSizeMapping(sizemap).addService(googletag.pubads());sizemap = googletag.sizeMapping().addSize([ 970, 0 ], [[300,250]]).addSize([ 300, 0 ], [[300,250]]).addSize([ 0, 0 ], [[1,1]]).build();                    googletag.defineSlot('/24669334/tc_300_new_2', [[300,250],[300,250]], 'div-db-2').defineSizeMapping(sizemap).addService(googletag.pubads());            });

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
                }            });
        </script>
        <script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/js/main.min.js?ver=7.0.0.5' id='main-script-js'></script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/js/pwa.min.js?ver=7.0.0.5' id='pwa-script-js'></script>
<script type='text/javascript' src='//x7d4c5z5.stackpathcdn.com/wp-content/themes/tc2.0/js/news-tagging.min.js?ver=2.0' id='news-tag-js'></script>
<script type='text/javascript' src='https://cdn.onesignal.com/sdks/OneSignalSDK.js?ver=6.0.2' async='async' id='remote_sdk-js'></script>
</body>
</html>
'''
blogger = Parser({
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
      "_01st_january_1970"
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
         2
      ],
      "contents"
   ],
   "terminator":"Share this article",
   "unwanted_blocks":[
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
"bad_signatures": [[["div", "class", "site-desc", "0"], "text", "TechCabal"]]
})
blogger.extract('nans', input)
