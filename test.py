import re

test = '''
<!DOCTYPE html>
<!--[if IE 8]> <html class="ie ie8" lang="en-GB"> <![endif]-->
<!--[if IE 9]> <html class="ie ie9" lang="en-GB"> <![endif]-->
<!--[if gt IE 9]><!--> <html lang="en-GB"> <!--<![endif]-->
<head>
<meta charset="UTF-8" />
<title>East Africa Archives - Disrupt Africa</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<link rel="pingback" href="https://disrupt-africa.com/xmlrpc.php" />
<link rel="shortcut icon" href="https://disrupt-africa.com/wp-content/uploads/2014/11/disrupt-icon.ico" />
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

<link rel="canonical" href="https://disrupt-africa.com/category/region/east-africa/" />
<link rel="next" href="https://disrupt-africa.com/category/region/east-africa/page/2/" />
<meta property="og:locale" content="en_GB" />
<meta property="og:type" content="article" />
<meta property="og:title" content="East Africa Archives - Disrupt Africa" />
<meta property="og:url" content="https://disrupt-africa.com/category/region/east-africa/" />
<meta property="og:site_name" content="Disrupt Africa" />
<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://disrupt-africa.com/#website","url":"https://disrupt-africa.com/","name":"Disrupt Africa","description":"Startup | Invest | Disrupt","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://disrupt-africa.com/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-GB"},{"@type":"ImageObject","inLanguage":"en-GB","@id":"https://disrupt-africa.com/category/region/east-africa/#primaryimage","url":"https://disrupt-africa.com/wp-content/uploads/2022/08/Jihan-Abass.jpg","contentUrl":"https://disrupt-africa.com/wp-content/uploads/2022/08/Jihan-Abass.jpg","width":900,"height":484},{"@type":"CollectionPage","@id":"https://disrupt-africa.com/category/region/east-africa/","url":"https://disrupt-africa.com/category/region/east-africa/","name":"East Africa Archives - Disrupt Africa","isPartOf":{"@id":"https://disrupt-africa.com/#website"},"primaryImageOfPage":{"@id":"https://disrupt-africa.com/category/region/east-africa/#primaryimage"},"image":{"@id":"https://disrupt-africa.com/category/region/east-africa/#primaryimage"},"thumbnailUrl":"https://disrupt-africa.com/wp-content/uploads/2022/08/Jihan-Abass.jpg","breadcrumb":{"@id":"https://disrupt-africa.com/category/region/east-africa/#breadcrumb"},"inLanguage":"en-GB"},{"@type":"BreadcrumbList","@id":"https://disrupt-africa.com/category/region/east-africa/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://disrupt-africa.com/"},{"@type":"ListItem","position":2,"name":"Region","item":"https://disrupt-africa.com/category/region/"},{"@type":"ListItem","position":3,"name":"East Africa"}]}]}</script>

<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="Disrupt Africa &raquo; Feed" href="https://disrupt-africa.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="Disrupt Africa &raquo; Comments Feed" href="https://disrupt-africa.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="Disrupt Africa &raquo; East Africa Category Feed" href="https://disrupt-africa.com/category/region/east-africa/feed/" />

<script src="//www.googletagmanager.com/gtag/js?id=UA-56899418-1" data-cfasync="false" data-wpfc-render="false" type="text/javascript" async></script>
<script data-cfasync="false" data-wpfc-render="false" type="text/javascript">
				var em_version = '7.7.0';
				var em_track_user = true;
				var em_no_track_reason = '';
				
								var disableStrs = [
										'ga-disable-G-MR1W91Y1DD',
															'ga-disable-UA-56899418-1',
									];

				/* Function to detect opted out users */
				function __gtagTrackerIsOptedOut() {
					for ( var index = 0; index < disableStrs.length; index++ ) {
						if ( document.cookie.indexOf( disableStrs[ index ] + '=true' ) > -1 ) {
							return true;
						}
					}

					return false;
				}

				/* Disable tracking if the opt-out cookie exists. */
				if ( __gtagTrackerIsOptedOut() ) {
					for ( var index = 0; index < disableStrs.length; index++ ) {
						window[ disableStrs[ index ] ] = true;
					}
				}

				/* Opt-out function */
				function __gtagTrackerOptout() {
					for ( var index = 0; index < disableStrs.length; index++ ) {
						document.cookie = disableStrs[ index ] + '=true; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/';
						window[ disableStrs[ index ] ] = true;
					}
				}

				if ( 'undefined' === typeof gaOptout ) {
					function gaOptout() {
						__gtagTrackerOptout();
					}
				}
								window.dataLayer = window.dataLayer || [];

				window.ExactMetricsDualTracker = {
					helpers: {},
					trackers: {},
				};
				if ( em_track_user ) {
					function __gtagDataLayer() {
						dataLayer.push( arguments );
					}

					function __gtagTracker( type, name, parameters ) {
						if (!parameters) {
							parameters = {};
						}

						if (parameters.send_to) {
							__gtagDataLayer.apply( null, arguments );
							return;
						}

						if ( type === 'event' ) {
															parameters.send_to = exactmetrics_frontend.v4_id;
								var hookName = name;
								if ( typeof parameters[ 'event_category' ] !== 'undefined' ) {
									hookName = parameters[ 'event_category' ] + ':' + name;
								}

								if ( typeof ExactMetricsDualTracker.trackers[ hookName ] !== 'undefined' ) {
									ExactMetricsDualTracker.trackers[ hookName ]( parameters );
								} else {
									__gtagDataLayer( 'event', name, parameters );
								}
							
															parameters.send_to = exactmetrics_frontend.ua;
								__gtagDataLayer( type, name, parameters );
													} else {
							__gtagDataLayer.apply( null, arguments );
						}
					}
					__gtagTracker( 'js', new Date() );
					__gtagTracker( 'set', {
						'developer_id.dNDMyYj' : true,
											} );
										__gtagTracker( 'config', 'G-MR1W91Y1DD', {"forceSSL":"true"} );
															__gtagTracker( 'config', 'UA-56899418-1', {"forceSSL":"true"} );
										window.gtag = __gtagTracker;											(function () {
							/* https://developers.google.com/analytics/devguides/collection/analyticsjs/ */
							/* ga and __gaTracker compatibility shim. */
							var noopfn = function () {
								return null;
							};
							var newtracker = function () {
								return new Tracker();
							};
							var Tracker = function () {
								return null;
							};
							var p = Tracker.prototype;
							p.get = noopfn;
							p.set = noopfn;
							p.send = function (){
								var args = Array.prototype.slice.call(arguments);
								args.unshift( 'send' );
								__gaTracker.apply(null, args);
							};
							var __gaTracker = function () {
								var len = arguments.length;
								if ( len === 0 ) {
									return;
								}
								var f = arguments[len - 1];
								if ( typeof f !== 'object' || f === null || typeof f.hitCallback !== 'function' ) {
									if ( 'send' === arguments[0] ) {
										var hitConverted, hitObject = false, action;
										if ( 'event' === arguments[1] ) {
											if ( 'undefined' !== typeof arguments[3] ) {
												hitObject = {
													'eventAction': arguments[3],
													'eventCategory': arguments[2],
													'eventLabel': arguments[4],
													'value': arguments[5] ? arguments[5] : 1,
												}
											}
										}
										if ( 'pageview' === arguments[1] ) {
											if ( 'undefined' !== typeof arguments[2] ) {
												hitObject = {
													'eventAction': 'page_view',
													'page_path' : arguments[2],
												}
											}
										}
										if ( typeof arguments[2] === 'object' ) {
											hitObject = arguments[2];
										}
										if ( typeof arguments[5] === 'object' ) {
											Object.assign( hitObject, arguments[5] );
										}
										if ( 'undefined' !== typeof arguments[1].hitType ) {
											hitObject = arguments[1];
											if ( 'pageview' === hitObject.hitType ) {
												hitObject.eventAction = 'page_view';
											}
										}
										if ( hitObject ) {
											action = 'timing' === arguments[1].hitType ? 'timing_complete' : hitObject.eventAction;
											hitConverted = mapArgs( hitObject );
											__gtagTracker( 'event', action, hitConverted );
										}
									}
									return;
								}

								function mapArgs( args ) {
									var arg, hit = {};
									var gaMap = {
										'eventCategory': 'event_category',
										'eventAction': 'event_action',
										'eventLabel': 'event_label',
										'eventValue': 'event_value',
										'nonInteraction': 'non_interaction',
										'timingCategory': 'event_category',
										'timingVar': 'name',
										'timingValue': 'value',
										'timingLabel': 'event_label',
										'page' : 'page_path',
										'location' : 'page_location',
										'title' : 'page_title',
									};
									for ( arg in args ) {
																				if ( ! ( ! args.hasOwnProperty(arg) || ! gaMap.hasOwnProperty(arg) ) ) {
											hit[gaMap[arg]] = args[arg];
										} else {
											hit[arg] = args[arg];
										}
									}
									return hit;
								}

								try {
									f.hitCallback();
								} catch ( ex ) {
								}
							};
							__gaTracker.create = newtracker;
							__gaTracker.getByName = newtracker;
							__gaTracker.getAll = function () {
								return [];
							};
							__gaTracker.remove = noopfn;
							__gaTracker.loaded = true;
							window['__gaTracker'] = __gaTracker;
						})();
									} else {
										console.log( "" );
					( function () {
							function __gtagTracker() {
								return null;
							}
							window['__gtagTracker'] = __gtagTracker;
							window['gtag'] = __gtagTracker;
					} )();
									}
			</script>

<script type="text/javascript">
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/disrupt-africa.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.0.1"}};
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
<link rel='stylesheet' id='sdm-styles-css' href='https://disrupt-africa.com/wp-content/plugins/simple-download-monitor/css/sdm_wp_styles.css?ver=6.0.1' type='text/css' media='all' />
<link rel='stylesheet' id='wp-block-library-css' href='https://disrupt-africa.com/wp-includes/css/dist/block-library/style.min.css?ver=6.0.1' type='text/css' media='all' />
<style id='wp-block-library-inline-css' type='text/css'>
.has-text-align-justify{text-align:justify;}
</style>
<link rel='stylesheet' id='mediaelement-css' href='https://disrupt-africa.com/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.16' type='text/css' media='all' />
<link rel='stylesheet' id='wp-mediaelement-css' href='https://disrupt-africa.com/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=6.0.1' type='text/css' media='all' />
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
</style>
<link rel='stylesheet' id='contact-form-7-css' href='https://disrupt-africa.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='mailerlite_forms.css-css' href='https://disrupt-africa.com/wp-content/plugins/official-mailerlite-sign-up-forms/assets/css/mailerlite_forms.css?ver=1.5.9' type='text/css' media='all' />
<link rel='stylesheet' id='wordpress-popular-posts-css-css' href='https://disrupt-africa.com/wp-content/plugins/wordpress-popular-posts/assets/css/wpp.css?ver=6.0.3' type='text/css' media='all' />
<link rel='stylesheet' id='parente2-style-css' href='https://disrupt-africa.com/wp-content/themes/smart-mag/style.css?ver=6.0.1' type='text/css' media='all' />
<link rel='stylesheet' id='childe2-style-css' href='https://disrupt-africa.com/wp-content/themes/smart-mag-child/style.css?ver=6.0.1' type='text/css' media='all' />
<link rel='stylesheet' id='smartmag-fonts-css' href='https://fonts.googleapis.com/css?family=Open+Sans%3A400%2C400Italic%2C600%2C700%7CRoboto+Slab&#038;subset' type='text/css' media='all' />
<link rel='stylesheet' id='smartmag-core-css' href='https://disrupt-africa.com/wp-content/themes/smart-mag-child/style.css?ver=3.4.0' type='text/css' media='all' />
<link rel='stylesheet' id='smartmag-responsive-css' href='https://disrupt-africa.com/wp-content/themes/smart-mag/css/responsive.css?ver=3.4.0' type='text/css' media='all' />
<link rel='stylesheet' id='smartmag-font-awesome-css' href='https://disrupt-africa.com/wp-content/themes/smart-mag/css/fontawesome/css/font-awesome.min.css?ver=3.4.0' type='text/css' media='all' />
<style id='smartmag-font-awesome-inline-css' type='text/css'>
@import url('https://fonts.googleapis.com/css?family=Roboto+Slab%3Aregular&subset=');


.navigation { background-color: #077fff;; }

@media only screen and (max-width: 799px) { .navigation .menu > li:hover > a, .navigation .menu > .current-menu-item > a, 
.navigation .menu > .current-menu-parent > a { background-color: #077fff;; } }

.navigation.sticky { background: rgb(7,127,255); background: rgba(7,127,255, 0.9);; }

.navigation .mega-menu, .navigation .menu ul { background-color: #077fff;; }

@media only screen and (max-width: 799px) { .navigation .mega-menu.links > li:hover { background-color: #077fff;; } }

.navigation .menu > li:hover, .navigation .menu li li:hover, .navigation .menu li li.current-menu-item,
.navigation .mega-menu .sub-nav li:hover, .navigation .menu .sub-nav li.current-menu-item { background-color: #f8ca00;; }

@media only screen and (max-width: 799px) { .navigation .menu > li:hover > a, .navigation .menu > .current-menu-item > a, 
.navigation .menu > .current-menu-parent > a, .navigation .mega-menu.links > li:hover,
.navigation .menu > .current-menu-ancestor > a, .navigation .menu li.active { background-color: #f8ca00;; } }

.main .sidebar .widgettitle, .tabbed .tabs-list { background-color: #077fff;; }

.navigation a, .mega-menu .heading, .mega-menu .featured h2 a { color: #161616;; }

.navigation { border-color: #077fff;; }

.navigation .menu > li li a, .navigation .mega-menu.links > li > a, .navigation .mega-menu.links > li li a,
.mega-menu .posts-list .content, .navigation .mega-menu .sub-nav li a { border-color: #077fff;; }

@media only screen and (max-width: 799px) { .navigation .menu li a { border-color: #077fff;; } }

.post-header h1, .post-content h1, .post-content h2, .post-content h3, .post-content h4, .post-content h5, .post-content h6 { font-family: "Roboto Slab", Arial, sans-serif; font-weight: normal; }
::selection { background: #077fff; }

::-moz-selection { background: #077fff; }

.top-bar, .post-content .modern-quote, .mobile-head { border-top-color: #077fff; }

.main-color,
.trending-ticker .heading,
.nav-light .menu > li:hover > a,
.nav-light .menu > .current-menu-item > a,
.nav-light .menu > .current-menu-parent > a,
.nav-light .menu li li:hover,
.nav-light .menu li li.current-menu-item,
.nav-light .mega-menu .sub-nav li:hover,
.nav-light .menu .sub-nav li.current-menu-item,
.nav-light .menu li li:hover > a,
.nav-light .menu li li.current-menu-item > a,
.nav-light .mega-menu .sub-nav li:hover > a,
.nav-light .menu .sub-nav li.current-menu-item > a,
.nav-light-search .active .search-icon,
.nav-light-search .search-icon:hover,
.breadcrumbs .location,
.gallery-title,
.section-head.prominent,
.recentcomments .url,
.block.posts .fa-angle-right,
.news-focus .section-head,
.focus-grid .section-head,
.post-meta-b .posted-by a,
.post-content a,
.main-stars,
.main-stars span:before,
.related-posts .section-head,
.comments-list .bypostauthor .comment-author a,
.error-page .text-404,
a.bbp-author-name { color: #077fff; }

.navigation .menu > li:hover > a,
.navigation .menu > .current-menu-item > a,
.navigation .menu > .current-menu-parent > a,
.navigation .menu > .current-menu-ancestor > a,
.block-head,
.tabbed .tabs-list .active a,
.comment-content .reply,
.sc-tabs .active a,
.nav-dark-b { border-bottom-color: #077fff; }

.main-featured .cat,
.main-featured .pages .flex-active,
.main-pagination .current,
.main-pagination a:hover,
.block-head .heading,
.cat-title,
.post .read-more a,
.rate-number .progress,
.listing-meta .rate-number .progress,
.review-box .overall,
.review-box .bar,
.post-pagination > span,
.button,
.sc-button-default:hover,
.drop-caps { background: #077fff; }

.nav-search .search-icon:hover,
.nav-search .active .search-icon { border-color: #077fff; }

.modal-header .modal-title,
.highlights h2:before,
.post-header .post-title:before,
.review-box .heading,
.main-heading,
.page-title,
.entry-title,
div.bbp-template-notice,
div.indicator-hint,
div.bbp-template-notice.info,
.post-content .wpcf7-not-valid-tip { border-left-color: #077fff; }

@media only screen and (max-width: 799px) { .navigation .mobile .fa { background: #077fff; } }

.mobile-head { border-top-color: #077fff; }

.post-content a { color: #077fff; }

.post-content h1 { font-size: 22px;; }

.post-content h2 { font-size: 18px;; }

.post-content h3 { font-size: 16px;; }

.post-content h4 { font-size: 14px;; }

.post-content h5 { font-size: 12px;; }

.post-content h6 { font-size: 12px;; }


.cat-15, 
.cat-title.cat-15,
.block-head.cat-text-15 .heading { 
	background: #d70060;
}

.block-head.cat-text-15 {
	border-color: #d70060;
}
				
.cat-text-15, .section-head.cat-text-15 { color: #d70060; }
				 

.navigation .menu > .menu-cat-15:hover > a, .navigation .menu > .menu-cat-15.current-menu-item > a, .navigation .menu > .menu-cat-15.current-menu-parent > a {
	border-bottom-color: #d70060;
}

body.boxed.category-15 { background: url(https://theme-sphere.com/smart-mag/wp-content/uploads/2013/07/9278066227_ae25452933_b1.jpg) no-repeat center center fixed; -webkit-background-size: cover; background-size: cover; }

.cat-14, 
.cat-title.cat-14,
.block-head.cat-text-14 .heading { 
	background: #2980b9;
}

.block-head.cat-text-14 {
	border-color: #2980b9;
}
				
.cat-text-14, .section-head.cat-text-14 { color: #2980b9; }
				 

.navigation .menu > .menu-cat-14:hover > a, .navigation .menu > .menu-cat-14.current-menu-item > a, .navigation .menu > .menu-cat-14.current-menu-parent > a {
	border-bottom-color: #2980b9;
}


.cat-19, 
.cat-title.cat-19,
.block-head.cat-text-19 .heading { 
	background: #32742c;
}

.block-head.cat-text-19 {
	border-color: #32742c;
}
				
.cat-text-19, .section-head.cat-text-19 { color: #32742c; }
				 

.navigation .menu > .menu-cat-19:hover > a, .navigation .menu > .menu-cat-19.current-menu-item > a, .navigation .menu > .menu-cat-19.current-menu-parent > a {
	border-bottom-color: #32742c;
}


.cat-16, 
.cat-title.cat-16,
.block-head.cat-text-16 .heading { 
	background: #32742c;
}

.block-head.cat-text-16 {
	border-color: #32742c;
}
				
.cat-text-16, .section-head.cat-text-16 { color: #32742c; }
				 

.navigation .menu > .menu-cat-16:hover > a, .navigation .menu > .menu-cat-16.current-menu-item > a, .navigation .menu > .menu-cat-16.current-menu-parent > a {
	border-bottom-color: #32742c;
}


.cat-17, 
.cat-title.cat-17,
.block-head.cat-text-17 .heading { 
	background: #e67e22;
}

.block-head.cat-text-17 {
	border-color: #e67e22;
}
				
.cat-text-17, .section-head.cat-text-17 { color: #e67e22; }
				 

.navigation .menu > .menu-cat-17:hover > a, .navigation .menu > .menu-cat-17.current-menu-item > a, .navigation .menu > .menu-cat-17.current-menu-parent > a {
	border-bottom-color: #e67e22;
}


.cat-18, 
.cat-title.cat-18,
.block-head.cat-text-18 .heading { 
	background: #3498db;
}

.block-head.cat-text-18 {
	border-color: #3498db;
}
				
.cat-text-18, .section-head.cat-text-18 { color: #3498db; }
				 

.navigation .menu > .menu-cat-18:hover > a, .navigation .menu > .menu-cat-18.current-menu-item > a, .navigation .menu > .menu-cat-18.current-menu-parent > a {
	border-bottom-color: #3498db;
}


.cat-3, 
.cat-title.cat-3,
.block-head.cat-text-3 .heading { 
	background: #d70060;
}

.block-head.cat-text-3 {
	border-color: #d70060;
}
				
.cat-text-3, .section-head.cat-text-3 { color: #d70060; }
				 

.navigation .menu > .menu-cat-3:hover > a, .navigation .menu > .menu-cat-3.current-menu-item > a, .navigation .menu > .menu-cat-3.current-menu-parent > a {
	border-bottom-color: #d70060;
}

body.boxed.category-3 { background: url(https://theme-sphere.com/smart-mag/wp-content/uploads/2013/07/9278066227_ae25452933_b1.jpg) no-repeat center center fixed; -webkit-background-size: cover; background-size: cover; }

.cat-12, 
.cat-title.cat-12,
.block-head.cat-text-12 .heading { 
	background: #d4301a;
}

.block-head.cat-text-12 {
	border-color: #d4301a;
}
				
.cat-text-12, .section-head.cat-text-12 { color: #d4301a; }
				 

.navigation .menu > .menu-cat-12:hover > a, .navigation .menu > .menu-cat-12.current-menu-item > a, .navigation .menu > .menu-cat-12.current-menu-parent > a {
	border-bottom-color: #d4301a;
}


.cat-4, 
.cat-title.cat-4,
.block-head.cat-text-4 .heading { 
	background: #32742c;
}

.block-head.cat-text-4 {
	border-color: #32742c;
}
				
.cat-text-4, .section-head.cat-text-4 { color: #32742c; }
				 

.navigation .menu > .menu-cat-4:hover > a, .navigation .menu > .menu-cat-4.current-menu-item > a, .navigation .menu > .menu-cat-4.current-menu-parent > a {
	border-bottom-color: #32742c;
}


.cat-13, 
.cat-title.cat-13,
.block-head.cat-text-13 .heading { 
	background: #e67e22;
}

.block-head.cat-text-13 {
	border-color: #e67e22;
}
				
.cat-text-13, .section-head.cat-text-13 { color: #e67e22; }
				 

.navigation .menu > .menu-cat-13:hover > a, .navigation .menu > .menu-cat-13.current-menu-item > a, .navigation .menu > .menu-cat-13.current-menu-parent > a {
	border-bottom-color: #e67e22;
}


.cat-5, 
.cat-title.cat-5,
.block-head.cat-text-5 .heading { 
	background: #3498db;
}

.block-head.cat-text-5 {
	border-color: #3498db;
}
				
.cat-text-5, .section-head.cat-text-5 { color: #3498db; }
				 

.navigation .menu > .menu-cat-5:hover > a, .navigation .menu > .menu-cat-5.current-menu-item > a, .navigation .menu > .menu-cat-5.current-menu-parent > a {
	border-bottom-color: #3498db;
}



</style>
<link rel='stylesheet' id='jetpack_css-css' href='https://disrupt-africa.com/wp-content/plugins/jetpack/css/jetpack.css?ver=11.2' type='text/css' media='all' />
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/plugins/google-analytics-dashboard-for-wp/assets/js/frontend-gtag.js?ver=7.7.0' id='exactmetrics-frontend-script-js'></script>
<script data-cfasync="false" data-wpfc-render="false" type="text/javascript" id='exactmetrics-frontend-script-js-extra'>/* <![CDATA[ */
var exactmetrics_frontend = {"js_events_tracking":"true","download_extensions":"zip,mp3,mpeg,pdf,docx,pptx,xlsx,rar","inbound_paths":"[{\"path\":\"\\\/go\\\/\",\"label\":\"affiliate\"},{\"path\":\"\\\/recommend\\\/\",\"label\":\"affiliate\"}]","home_url":"https:\/\/disrupt-africa.com","hash_tracking":"false","ua":"UA-56899418-1","v4_id":"G-MR1W91Y1DD"};/* ]]> */
</script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-includes/js/jquery/jquery.min.js?ver=3.6.0' id='jquery-core-js'></script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2' id='jquery-migrate-js'></script>
<script type='text/javascript' id='sdm-scripts-js-extra'>
/* <![CDATA[ */
var sdm_ajax_script = {"ajaxurl":"https:\/\/disrupt-africa.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
</script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/plugins/simple-download-monitor/js/sdm_wp_scripts.js?ver=6.0.1' id='sdm-scripts-js'></script>
<script type='application/json' id='wpp-json'>
{"sampling_active":1,"sampling_rate":100,"ajax_url":"https:\/\/disrupt-africa.com\/wp-json\/wordpress-popular-posts\/v1\/popular-posts","api_url":"https:\/\/disrupt-africa.com\/wp-json\/wordpress-popular-posts","ID":0,"token":"30ae2c9aa3","lang":0,"debug":1}
</script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/plugins/wordpress-popular-posts/assets/js/wpp.min.js?ver=6.0.3' id='wpp-js-js'></script>
<link rel="https://api.w.org/" href="https://disrupt-africa.com/wp-json/" /><link rel="alternate" type="application/json" href="https://disrupt-africa.com/wp-json/wp/v2/categories/27" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://disrupt-africa.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://disrupt-africa.com/wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress 6.0.1" />

<script>
                (function (m, a, i, l, e, r) {
                    m['MailerLiteObject'] = e;

                    function f() {
                        var c = {a: arguments, q: []};
                        var r = this.push(c);
                        return "number" != typeof r ? r : f.bind(c.q);
                    }

                    f.q = f.q || [];
                    m[e] = m[e] || f.bind(f.q);
                    m[e].q = m[e].q || f.q;
                    r = a.createElement(i);
                    var _ = a.getElementsByTagName(i)[0];
                    r.async = 1;
                    r.src = l + '?' + (~~(new Date().getTime() / 10000000));
                    _.parentNode.insertBefore(r, _);
                })(window, document, 'script', 'https://static.mailerlite.com/js/universal.js', 'ml');

                var ml_account = ml('accounts', '1158398', 'q6m7p2b7s6', 'load');
            </script>

<style id="wpp-loading-animation-styles">@-webkit-keyframes bgslide{from{background-position-x:0}to{background-position-x:-200%}}@keyframes bgslide{from{background-position-x:0}to{background-position-x:-200%}}.wpp-widget-placeholder,.wpp-widget-block-placeholder{margin:0 auto;width:60px;height:3px;background:#dd3737;background:linear-gradient(90deg,#dd3737 0%,#571313 10%,#dd3737 100%);background-size:200% auto;border-radius:3px;-webkit-animation:bgslide 1s infinite linear;animation:bgslide 1s infinite linear}</style>
<style>img#wpstats{display:none}</style>
<style type="text/css" id="wp-custom-css">
			.page>.row.builder .textwidget.post-content {
	margin-bottom: 0 !important;
}

.column.builder.one-1 {
    height: max-content !important;
}

.posts-list .content time {
    margin-top: 5px;
}

.grid-overlay article .image-link {
    display: block;
    max-height: 175px;
    overflow: hidden;
}


.main-featured{
	margin-bottom: 0px;
}

.main.wrap.cf {
   margin-top: 5px;
}

.main-featured .pages .flex-active{
	background: transparent;
}

#social-table th, #social-table td, #social-table tr{
	background: white;
	border: none;	
}

@media only screen and (max-width: 767px){
	article.small h3 {font-size: 75% !important;}
	.blocks.col-4 { padding:25px;}
}
.main-featured .blocks {
    display: block !important;
	
}
.live-search-results.fade-in {
    display: none !important;
}

.menu-sub-menu-container.navigation.cf.nav-dark.ragion_menu.wrap.margin_top {
    max-width: 95%;
}

@media only screen and (max-width: 799px) and (min-width: 768px){
.main-featured .slider, .main-featured .flexslider{
    width: 65%;
    height:219px !important;
}li.flex-active-slide {
    max-width: 500px !important;

}
}



/* .col-6.item.small-item:last-child{ display: none; }
.attachment-grid-slider-small.size-grid-slider-small.wp-post-image.lazyloaded{ max-height: 108px;}
.featured-grid .small-item .image-link{ min-height: 127.5px; } */

.post-header .featured .caption, .post-header-b .featured .caption {
font-size: 12px;
}
.post-header .post-meta.cf .cats {
    display: none !important;
}

nav.navigation.cf.nav-full.nav-dark {
    width: 1078px !important;
    margin: 0 auto;
}
.navigation.cf.nav-full.nav-dark .wrap {
    padding: 0px !important;
}

.blocks.col-4 {display:block !important;}
.navigation .menu > li > a{ font-weight: bold; }
li#menu-item-2197,.current-menu-item{background: #f8ca00}
.mailerlite-form-title{
	background-color: #077fff;
  text-transform: uppercase;
  padding: 0 14px;
  line-height: 34px;
  margin-bottom: 10px;
}
.gallery-title, .section-head.prominent {
    color: #ffffff;
}
.mailerlite-form-title h3{
	font-family: "Open Sans", Arial, sans-serif;
  font-size: 13px;
	color: white;
} 
.gallery-title, .section-head {
    background: #077fff;
    border: 1px solid #d9d9d9;
    border-left: 0;
    border-right: 0;
    line-height: 32px;
    color: #ffffff;
    font-size: 13px;
    font-family: open sans,Arial,sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    padding: 0 14px;
    margin-bottom: 28px;
}
.main-head .adwrap-widget, .main-head .a-widget {
    padding-top: 40px;
}



.tribe-events-calendar thead th, #tribe-bar-collapse-toggle, #tribe-bar-collapse-toggle:hover, #tribe-bar-collapse-toggle:focus, #tribe-bar-collapse-toggle:hover, #tribe-bar-views-toggle, #tribe-bar-views-toggle:hover, #tribe-bar-views-toggle:focus, #tribe-bar-form .tribe-bar-submit input[type=submit], .tribe-bar-views-inner {
		background-color: #077fff;
		color: black;
}

.tribe-event-featured, .tribe-events-calendar div[id*="tribe-events-daynum-"]{
	background-color: #077fff !important;
	color: black !important;
}

#tribe-events .tribe-events-calendar td.tribe-events-othermonth, #tribe-events .tribe-grid-allday, #tribe-events .tribe-events-calendar td:hover{
	background-color: #077fff03;
}
#tribe-bar-form.tribe-bar-collapse .tribe-bar-filters, .datepicker-months, #tribe-bar-views .tribe-bar-views-list, #tribe-events .tribe-events-calendar td{
	background-color: white;
}

#tribe-events-content table.tribe-events-calendar .type-tribe_events.tribe-event-featured .tribe-events-month-event-title a {
    color: black;
}

#tribe-bar-views .tribe-bar-views-option.tribe-bar-active, #tribe-bar-views .tribe-bar-views-option:hover, .tribe-events-list .tribe-events-loop {
	background-color: #f9f9f9;
}

.tribe-events-list .tribe-events-loop, #tribe-events-content a, .tribe-events-adv-list-widget .tribe-events-widget-link a, .tribe-events-adv-list-widget .tribe-events-widget-link a:hover, .tribe-events-back a, .tribe-events-back a:hover, .tribe-events-event-meta a, .tribe-events-list-widget .tribe-events-widget-link a, .tribe-events-list-widget .tribe-events-widget-link a:hover, ul.tribe-events-sub-nav a, ul.tribe-events-sub-nav a:hover{
	border-top: 1px solid #d9d9d9;
	background: white;
}

#tribe-events-content a{
	border: none;
	background-color:transparent;
}

.tribe-events-day .tribe-events-day-time-slot .tribe-events-day-time-slot-heading{
	color: black;
	background-color: #077fff;
}

.tribe-events-list .tribe-events-loop .tribe-event-featured .tribe-events-event-meta, .tribe-events-list .tribe-events-loop .tribe-event-featured .tribe-events-event-cost span, .tribe-events-list .tribe-events-loop .tribe-event-featured .tribe-events-content{
/* 	color: black; */
}

.tribe-events-viewmore {
    border-top: 1px solid #e7e7e7;
    font-weight: 700;
    line-height: 1;
    margin: 0 5%;
    padding: 0px 0px;
    font-size: 10px;
}

.tribe-bar-submit{
    width: 100%;
    margin: auto;
}

@media only screen and (max-width: 900px) {
.tribe-events-list .tribe-events-venue-details, .tribe-events-loop .tribe-events-event-meta {
    border: none;
}
}

.tribe-events-schedule h2{
	font-weight: 100;
	font-size: 14px
}

.tribe-events-filters-horizontal .tribe-events-filters-content, .tribe_events_filters_wrapper, #tribe_events_filters_wrapper.tribe-events-filters-horizontal, #tribe_events_filters_wrapper.tribe-events-filters-horizontal, .tribe-filters-closed #tribe_events_filters_wrapper.tribe-events-filters-horizontal {
    background: #297ef8;
    border: 1px solid #297df8;
}
#tribe_events_filters_wrapper .tribe_events_slider_val, #tribe_events_filters_wrapper.tribe-events-filters-horizontal .tribe-events-filters-label{
	color: black;
}

.tribe-events-filters-horizontal .tribe-events-filter-group{
		background-color: #f9fafa;
    border: 1px solid #0000000d;
}
.tribe-events-filters-horizontal #tribe_events_filter_control a{
	color: #0000007d;
}

#tribe-events-content-wrapper, #tribe-events-content{
	width: 80% !important;
	margin: auto;
}
.tribe-events-loop{
	max-width:100%;
}

.single-tribe_events .tribe-events-single-event-title{
	font-size: 1.4em;
	color: #19232d;
}
.single-tribe_events{
	font-size: 13px;
	color: #606569;
}

/* THis codes use for submenu bellow the main navigation */
.menu-sub-menu-container.navigation.cf.nav-dark.ragion_menu.wrap.margin_top {
    margin-top: 15px !important;
	  padding:0px;
}
.menu-sub-menu-container.navigation.cf.nav-dark.ragion_menu.wrap.margin_top ul li {
    width: 25%;
    
}
.menu-sub-menu-container.navigation.cf.nav-dark.ragion_menu.wrap.margin_top ul li a{
  width:80%!important;
 display:inline-block;
text-align:center;
}

ul.zoom-social-icons-list.zoom-social-icons-list--with-canvas.zoom-social-icons-list--square.zoom-social-icons-list--align-center.zoom-social-icons-list--no-labels{
	float: right;
}
/* This code use for footer */
.lower-foot {
    font-size: 14px;
    padding: 20px;
}
span.cat-title {
    display: none;
}
/* this code use for Right Side Posts Grid besides the header slider */
/* .blocks.col-4 article{
    height: 110px !important;
    width:100%;
    overflow:hidden;
margin:0 !important;
padding:0 !important;
}

.blocks.col-4 article img {
    width: 100% !important;
    height: auto !important;
    transform: translate(0px, -10px);
} */


.page-content .widget-title {
    font-weight: 600;
    font-size: 13px;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 24px;
    background: #077fff;
    padding: 5px 10px;
    font-family: inherit;
    line-height: 1.5;
}
.slides .flex-active-slide a.cat.cat-title.cat-40 {
    display: none;
}

.slider ul.flex-direction-nav {
    display: none;
}

/* Display none on the first child of the right side content of the slider */
/* .wrap.cf .appear .blocks article:first-child {
    display: none !important;
} */

article.medium{
    height: 112px !important;
    overflow: hidden;
}

@media only screen and (max-width: 767px)
.main-featured .blocks {
    display: block;
}
/*category pages slider remove*/
body.category div.main-featured {
    display: none!important;
}
/*sponserd section remove*/
/* section.block-wrap.blog {
    display: none;
} */
/* mobile menu bar icon color*/
@media only screen and (max-width: 799px)
.navigation .mobile .hamburger, .navigation .mobile .fa-search {

    color: #000000!important;

}
/* Event section problem solution */
.column.builder.two-third h3.widget-title {
    display: none;
}
h3.widget-title-visible {
    display: block !important;
}
.textwidget .widget-title a {
    color: white;;
}
.two-third ul.posts-list {
    padding-top: 40px;
}
a.cat.cat-title {
    display: none;
}

.column.builder.one-1{
		height: 0px;
}

.row.cf.builder{
	margin: 0;
}

/* Simple Download Monitor */
.sdm_fancy2_item {
    margin: none !important;
    border: none  !important;
    float: left  !important;
    width: 100%  !important;
}

a.sdm_fancy2_download_dl_link, .sdm_download {
    color: #161616!important;
		font-weight: bold;
    border-width: 6px!important;
    border-color: #077fff !important;
    background-color: #077fff !important;
	margin-top: 15px;
}

a.sdm_fancy2_download_dl_link:hover, .sdm_download:hover {
    color: #161616!important;
    border-width: 6px!important;
    border-color: #f8ca00 !important;
    background-color: #f8ca00 !important;
	padding: 10px 15px !important;
	border-radius: 3px;
}

.sdm_fancy2_download_title, .sdm_fancy2_download_date_label, .sdm_fancy2_download_date_value {
    margin: 10px 0;
    font-size: 100%;
    text-align: left !important;
		color: #19232d;
    font-size: 14px;
    font-family: "Roboto Slab", Georgia, serif !important;
}

a.sdm_download.green, a.sdm_download.green:hover {
    background: none;
    text-shadow: none;
    box-shadow: none;
		color: #19232d !important;
		text-decoration: none;
}

span.sdm_download_item_count {
    display: none;
}		</style>
<!--[if lt IE 9]>
<script src="https://disrupt-africa.com/wp-content/themes/smart-mag/js/html5.js" type="text/javascript"></script>
<![endif]-->
<script>
document.querySelector('head').innerHTML += '<style class="bunyad-img-effects-css">.main img, .main-footer img { opacity: 0; }</style>';
</script>
</head>
<body class="archive category category-east-africa category-27 page-builder right-sidebar full img-effects has-nav-dark has-head-default">
<div class="main-wrap">
<div class="top-bar dark">
<div class="wrap">
<section class="top-bar-content cf">
<div class="search">
<form role="search" action="https://disrupt-africa.com/" method="get">
<input type="text" name="s" class="query" value="" placeholder="Search..." />
<button class="search-button" type="submit"><i class="fa fa-search"></i></button>
</form>
</div> 
<div class="menu-top-bar-menu-container"><ul id="menu-top-bar-menu" class="menu"><li id="menu-item-2144" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2144"><a href="https://disrupt-africa.com/about/">About</a></li>
<li id="menu-item-2143" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2143"><a href="https://disrupt-africa.com/contact/">Contact</a></li>
<li id="menu-item-2278" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2278"><a href="https://disrupt-africa.com/advertise/">Advertise</a></li>
<li id="menu-item-21621" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21621"><a href="https://disrupt-africa.com/pipeline/">Pipeline</a></li>
<li id="menu-item-13200" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13200"><a href="https://disrupt-africa.com/research/">Research</a></li>
<li id="menu-item-21989" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21989"><a href="https://disrupt-africa.com/podcast/">Podcast</a></li>
</ul></div>
</section>
</div>
</div>
<div id="main-head" class="main-head">
<div class="wrap">
<header class="default">
<div class="title">
<a href="https://disrupt-africa.com/" title="Disrupt Africa" rel="home">
<img src="https://disrupt-africa.com/wp-content/uploads/2014/10/DA-logo-on-transparent-with-tag-small-e1414593297539.png" class="logo-image" alt="Disrupt Africa" />
</a> </div>
<div class="right">
<div class="a-widget">
<a href="https://disruptafrica.gumroad.com/l/qskzcl">
<img src=https://disrupt-africa.com/wp-content/uploads/2022/06/728-X-90-AD-4.png></a>
</div>
</div>
</header>
<div class="main-nav">
<div class="navigation-wrap cf">
<nav class="navigation cf nav-dark">
<div class>
<div class="mobile" data-type="off-canvas" data-search="1">
<a href="#" class="selected">
<span class="text">Navigate</span><span class="current"></span> <i class="hamburger fa fa-bars"></i>
</a>
</div>
<div class="menu-custom-main-container"><ul id="menu-custom-main" class="menu"><li id="menu-item-2197" class="yellow-menu-item menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-has-children menu-item-2197"><a href="https://disrupt-africa.com/">Home</a><ul class="mega-menu links row">
<li id="menu-item-2282" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-32 menu-item-2282"><a href="https://disrupt-africa.com/category/news/">News</a></li>
<li id="menu-item-2199" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-38 menu-item-2199"><a href="https://disrupt-africa.com/category/hubs/">Hubs</a></li>
<li id="menu-item-2351" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-37 menu-item-2351"><a href="https://disrupt-africa.com/category/startups/">Startups</a></li>
<li id="menu-item-2200" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-39 menu-item-2200"><a href="https://disrupt-africa.com/category/events/">Events</a></li>
<li id="menu-item-2198" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-40 menu-item-2198"><a href="https://disrupt-africa.com/category/features/">Features</a></li>
</ul>
</li>
</ul></div>
<div class="mobile-menu-container"><ul id="menu-sub-menu" class="menu mobile-menu"><li id="menu-item-24250" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-26 menu-item-24250"><a href="https://disrupt-africa.com/category/region/north-africa/">North Africa</a></li>
<li id="menu-item-24249" class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item menu-cat-27 menu-item-24249"><a href="https://disrupt-africa.com/category/region/east-africa/" aria-current="page">East Africa</a></li>
<li id="menu-item-24247" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-28 menu-item-24247"><a href="https://disrupt-africa.com/category/region/southern-africa/">Southern Africa</a></li>
<li id="menu-item-24248" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-29 menu-item-24248"><a href="https://disrupt-africa.com/category/region/west-africa/">West Africa</a></li>
</ul></div>
</div>
</nav>
</div>
</div>
</div>
</div>
<div class="menu-sub-menu-container navigation cf nav-dark ragion_menu wrap margin_top"><ul id="menu-sub-menu-1" class="menu"><li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-26 menu-item-24250"><a href="https://disrupt-africa.com/category/region/north-africa/">North Africa</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item menu-cat-27 menu-item-24249"><a href="https://disrupt-africa.com/category/region/east-africa/" aria-current="page">East Africa</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-28 menu-item-24247"><a href="https://disrupt-africa.com/category/region/southern-africa/">Southern Africa</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-cat-29 menu-item-24248"><a href="https://disrupt-africa.com/category/region/west-africa/">West Africa</a></li>
</ul></div>
<div class="main wrap cf">
<div class="row">
<div class="col-8 main-content">
<h2 class="main-heading">Browsing: <strong>East Africa</strong></h2>
<div class="row b-row listing meta-above grid-2">
<div class="column half b-col">
<article class="highlights post-30075 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-news tag-featured tag-lami">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/08/05/kenyan-insurtech-startup-lami-raises-us3-7m-seed-extension-round/" title="Kenyan insurtech startup Lami raises US$3.7m seed extension round" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2022/08/Jihan-Abass-351x185.jpg" class="image wp-post-image" alt="" title="Kenyan insurtech startup Lami raises US$3.7m seed extension round" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-08-05T08:00:51+02:00" class="meta-item">August 5, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/08/05/kenyan-insurtech-startup-lami-raises-us3-7m-seed-extension-round/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/08/05/kenyan-insurtech-startup-lami-raises-us3-7m-seed-extension-round/">Kenyan insurtech startup Lami raises US$3.7m seed extension round</a></h2>
<div class="excerpt"><p>Kenya-based B2B and B2B2C insurance-as-a-service platform and API Lami has raised a US$3.7 million seed&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30063 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-features category-north-africa category-southern-africa category-west-africa tag-featured tag-getihu tag-hi5 tag-seamlesshr tag-wyzetalk">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/08/04/opportunities-and-roadblocks-in-africas-nascent-hr-tech-space/" title="Opportunities and roadblocks in Africa’s nascent HR tech space" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2020/11/SeamlessHR-Pictures-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Opportunities and roadblocks in Africa’s nascent HR tech space" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-08-04T08:00:28+02:00" class="meta-item">August 4, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/08/04/opportunities-and-roadblocks-in-africas-nascent-hr-tech-space/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/08/04/opportunities-and-roadblocks-in-africas-nascent-hr-tech-space/">Opportunities and roadblocks in Africa’s nascent HR tech space</a></h2>
<div class="excerpt"><p>When Ryan Paterson and his co-founder Thomas Schmider launched their investment fund Getihu back in&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30044 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-events category-southern-africa category-west-africa tag-featured tag-mest-africa tag-mest-africa-challenge">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/08/03/applications-open-for-50k-mest-africa-challenge-2022/" title="Applications open for $50k MEST Africa Challenge 2022" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2019/06/MEST-Africa-Challenge-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Applications open for $50k MEST Africa Challenge 2022" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-08-03T09:00:29+02:00" class="meta-item">August 3, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/08/03/applications-open-for-50k-mest-africa-challenge-2022/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/08/03/applications-open-for-50k-mest-africa-challenge-2022/">Applications open for $50k MEST Africa Challenge 2022</a></h2>
<div class="excerpt"><p>MEST Africa has announced the opening of applications for the 2022 MEST Africa Challenge, the&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30052 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-hubs tag-cchub tag-featured tag-fintech-incubation-programme">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/08/02/rwandan-startups-invited-to-apply-for-2nd-fintech-incubation-programme/" title="Rwandan startups invited to apply for 2nd Fintech Incubation Programme" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2022/08/FIP-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Rwandan startups invited to apply for 2nd Fintech Incubation Programme" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-08-02T09:00:05+02:00" class="meta-item">August 2, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/08/02/rwandan-startups-invited-to-apply-for-2nd-fintech-incubation-programme/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/08/02/rwandan-startups-invited-to-apply-for-2nd-fintech-incubation-programme/">Rwandan startups invited to apply for 2nd Fintech Incubation Programme</a></h2>
<div class="excerpt"><p>Rwandan startups have been invited to apply for the second edition of the Fintech Innovation&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30041 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-news category-north-africa category-southern-africa category-west-africa tag-featured tag-oui-capital">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/08/02/africa-focused-vc-firm-oui-capital-launches-2nd-fund-to-double-down-on-startup-investments/" title="Africa-focused VC firm Oui Capital launches 2nd fund to double down on startup investments" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2022/08/OR2_6397-1-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Africa-focused VC firm Oui Capital launches 2nd fund to double down on startup investments" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-08-02T08:00:57+02:00" class="meta-item">August 2, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/08/02/africa-focused-vc-firm-oui-capital-launches-2nd-fund-to-double-down-on-startup-investments/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/08/02/africa-focused-vc-firm-oui-capital-launches-2nd-fund-to-double-down-on-startup-investments/">Africa-focused VC firm Oui Capital launches 2nd fund to double down on startup investments</a></h2>
<div class="excerpt"><p>Oui Capital, an Africa-focused venture capital firm, has announced the launch of its second fund,&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30035 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-hubs category-north-africa category-southern-africa category-west-africa tag-featured tag-hermenow">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/08/01/female-led-african-startups-invited-to-apply-for-hermenow-accelerator/" title="Female-led African startups invited to apply for HerMeNow accelerator" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2022/07/HerMeNow-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Female-led African startups invited to apply for HerMeNow accelerator" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-08-01T09:00:58+02:00" class="meta-item">August 1, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/08/01/female-led-african-startups-invited-to-apply-for-hermenow-accelerator/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/08/01/female-led-african-startups-invited-to-apply-for-hermenow-accelerator/">Female-led African startups invited to apply for HerMeNow accelerator</a></h2>
<div class="excerpt"><p>Women-led social enterprises in Africa and MENA that are building impactful solutions in culture, mindset,&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30007 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-news category-north-africa category-southern-africa category-west-africa tag-featured tag-seedstars">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/07/27/seedstars-announces-first-close-of-30m-emerging-market-seed-stage-fund/" title="Seedstars announces first close of $30m emerging market seed stage fund" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2022/07/3.-Seedstars-Founders-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Seedstars announces first close of $30m emerging market seed stage fund" srcset="https://disrupt-africa.com/wp-content/uploads/2022/07/3.-Seedstars-Founders-351x185.jpg 351w, https://disrupt-africa.com/wp-content/uploads/2022/07/3.-Seedstars-Founders-300x159.jpg 300w, https://disrupt-africa.com/wp-content/uploads/2022/07/3.-Seedstars-Founders.jpg 964w, https://disrupt-africa.com/wp-content/uploads/2022/07/3.-Seedstars-Founders-300x159@2x.jpg 600w" sizes="(max-width: 351px) 100vw, 351px" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-07-27T08:00:50+02:00" class="meta-item">July 27, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/07/27/seedstars-announces-first-close-of-30m-emerging-market-seed-stage-fund/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/07/27/seedstars-announces-first-close-of-30m-emerging-market-seed-stage-fund/">Seedstars announces first close of $30m emerging market seed stage fund</a></h2>
<div class="excerpt"><p>The Switzerland-based Seedstars has launched its second emerging market seed stage fund with a first&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-29989 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-hubs category-southern-africa category-west-africa tag-afrilabs tag-featured tag-unfpa">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/07/26/unfpa-afrilabs-launch-incubation-programme-to-support-ideas-tackling-fgm-climate-change/" title="UNFPA, AfriLabs launch incubation programme to support ideas tackling FGM, climate change" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2019/12/AfriLabs-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="UNFPA, AfriLabs launch incubation programme to support ideas tackling FGM, climate change" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-07-26T09:00:43+02:00" class="meta-item">July 26, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/07/26/unfpa-afrilabs-launch-incubation-programme-to-support-ideas-tackling-fgm-climate-change/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/07/26/unfpa-afrilabs-launch-incubation-programme-to-support-ideas-tackling-fgm-climate-change/">UNFPA, AfriLabs launch incubation programme to support ideas tackling FGM, climate change</a></h2>
<div class="excerpt"><p>The United Nations Population Fund and AfriLabs have launched an incubation programme aimed at supporting&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-30004 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-news category-west-africa tag-featured tag-y-combinator">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/07/26/4-african-startups-selected-for-s22-batch-of-y-combinator-accelerator/" title="4 African startups selected for S22 batch of Y Combinator accelerator" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2021/03/YC-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="4 African startups selected for S22 batch of Y Combinator accelerator" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-07-26T08:00:32+02:00" class="meta-item">July 26, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/07/26/4-african-startups-selected-for-s22-batch-of-y-combinator-accelerator/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/07/26/4-african-startups-selected-for-s22-batch-of-y-combinator-accelerator/">4 African startups selected for S22 batch of Y Combinator accelerator</a></h2>
<div class="excerpt"><p>Four African startups are among the initial 156 announced as participating in the S22 batch&hellip;</p>
</div>
</article>
</div>
<div class="column half b-col">
<article class="highlights post-29973 post type-post status-publish format-standard has-post-thumbnail category-east-africa category-hubs category-north-africa category-southern-africa category-west-africa tag-digital-square tag-featured">
<span class="cat-title cat-27"><a href="https://disrupt-africa.com/category/region/east-africa/" title="East Africa">East Africa</a></span>
<a href="https://disrupt-africa.com/2022/07/22/funding-opportunity-for-digital-entrepreneurs-in-the-health-space/" title="Funding opportunity for digital entrepreneurs in the health space" class="image-link">
<img width="351" height="185" src="https://disrupt-africa.com/wp-content/uploads/2015/07/health-351x185.jpg" class="image wp-post-image" alt="" loading="lazy" title="Funding opportunity for digital entrepreneurs in the health space" />
</a>
<div class="cf listing-meta meta above">
<time datetime="2022-07-22T09:00:20+02:00" class="meta-item">July 22, 2022</time><span class="meta-item comments"><a href="https://disrupt-africa.com/2022/07/22/funding-opportunity-for-digital-entrepreneurs-in-the-health-space/#respond"><i class="fa fa-comments-o"></i> 0</a></span>
</div>
<h2 class="post-title"><a href="https://disrupt-africa.com/2022/07/22/funding-opportunity-for-digital-entrepreneurs-in-the-health-space/">Funding opportunity for digital entrepreneurs in the health space</a></h2>
<div class="excerpt"><p>Digital Square, a PATH-led initiative funded by the United States Agency for International Development, the&hellip;</p>
</div>
</article>
</div>
</div>
<div class="main-pagination">
<span aria-current="page" class="page-numbers current">1</span>
<a class="page-numbers" href="https://disrupt-africa.com/category/region/east-africa/page/2/">2</a>
<a class="page-numbers" href="https://disrupt-africa.com/category/region/east-africa/page/3/">3</a>
<span class="page-numbers dots">&hellip;</span>
<a class="page-numbers" href="https://disrupt-africa.com/category/region/east-africa/page/338/">338</a>
<a class="next page-numbers" href="https://disrupt-africa.com/category/region/east-africa/page/2/"><span class="visuallyhidden">Next</span><i class="fa fa-angle-right"></i></a> </div>
</div>
<aside class="col-4 sidebar">
<div class="">
<ul>
<div class="widget-text wp_widget_plugin_box"><h3 class="widgettitle">DISRUPT AFRICA PODCAST</h3><li id="wp_soundpress_plugin-3" class="widget widget_wp_soundpress_plugin"><iframe width="100%" scrolling="no" height="auto" frameborder="no" src="https://w.soundcloud.com/player/?url=https://soundcloud.com/disruptafricapodcast&amp;show_user=true&amp;visual=true"></iframe><br /></li>
</div>
<li id="wpp-5" class="widget popular-posts">
<h3 class="widgettitle">MOST READ</h3>

<ul class="wpp-list wpp-cards">
<li class="">
<img src="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29830-featured-75x75.jpeg" srcset="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29830-featured-75x75.jpeg, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29830-featured-75x75@1.5x.jpeg 1.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29830-featured-75x75@2x.jpeg 2x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29830-featured-75x75@2.5x.jpeg 2.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29830-featured-75x75@3x.jpeg 3x" width="75" height="75" alt="" class="wpp-thumbnail wpp_featured wpp_cached_thumb" loading="lazy" />
<div class="wpp-item-data">
July 8, 2022
<h6 class="post-title"><a href="https://disrupt-africa.com/2022/07/08/tanzanian-startup-onilbox-is-a-fitness-tech-platform-with-continental-ambitions/" class="wpp-post-title" target="_self">Tanzanian startup OnilBox is a fitness tech platform with continental ambitions</a></h6>
</div>
</li>
<li class="">
<img src="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29977-featured-75x75.jpg" srcset="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29977-featured-75x75.jpg, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29977-featured-75x75@1.5x.jpg 1.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29977-featured-75x75@2x.jpg 2x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29977-featured-75x75@2.5x.jpg 2.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29977-featured-75x75@3x.jpg 3x" width="75" height="75" alt="" class="wpp-thumbnail wpp_featured wpp_cached_thumb" loading="lazy" />
<div class="wpp-item-data">
July 22, 2022
<h6 class="post-title"><a href="https://disrupt-africa.com/2022/07/22/ivory-coast-based-fintech-startup-bizao-raises-8-2m-to-expand-across-africa/" class="wpp-post-title" target="_self">Ivory Coast-based fintech startup Bizao raises $8.2m to expand across Africa</a></h6>
</div>
</li>
<li class="">
<img src="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29975-featured-75x75.jpg" srcset="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29975-featured-75x75.jpg, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29975-featured-75x75@1.5x.jpg 1.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29975-featured-75x75@2x.jpg 2x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29975-featured-75x75@2.5x.jpg 2.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29975-featured-75x75@3x.jpg 3x" width="75" height="75" alt="" class="wpp-thumbnail wpp_featured wpp_cached_thumb" loading="lazy" />
<div class="wpp-item-data">
July 25, 2022
<h6 class="post-title"><a href="https://disrupt-africa.com/2022/07/25/how-nigerias-remedial-health-is-making-africas-pharmaceutical-sector-more-efficient/" class="wpp-post-title" target="_self">How Nigeria’s Remedial Health is making Africa’s pharmaceutical sector more efficient</a></h6>
</div>
</li>
<li class="">
<img src="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29906-featured-75x75.jpg" srcset="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29906-featured-75x75.jpg, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29906-featured-75x75@1.5x.jpg 1.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29906-featured-75x75@2x.jpg 2x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29906-featured-75x75@2.5x.jpg 2.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29906-featured-75x75@3x.jpg 3x" width="75" height="75" alt="" class="wpp-thumbnail wpp_featured wpp_cached_thumb" loading="lazy" />
<div class="wpp-item-data">
July 14, 2022
<h6 class="post-title"><a href="https://disrupt-africa.com/2022/07/14/nigerian-fintech-infrastructure-startup-bloc-acquires-payments-company-orchestrate/" class="wpp-post-title" target="_self">Nigerian fintech infrastructure startup Bloc acquires payments company Orchestrate</a></h6>
</div>
</li>
<li class="">
<img src="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29890-featured-75x75.jpg" srcset="https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29890-featured-75x75.jpg, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29890-featured-75x75@1.5x.jpg 1.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29890-featured-75x75@2x.jpg 2x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29890-featured-75x75@2.5x.jpg 2.5x, https://disrupt-africa.com/wp-content/uploads/wordpress-popular-posts/29890-featured-75x75@3x.jpg 3x" width="75" height="75" alt="" class="wpp-thumbnail wpp_featured wpp_cached_thumb" loading="lazy" />
<div class="wpp-item-data">
July 13, 2022
<h6 class="post-title"><a href="https://disrupt-africa.com/2022/07/13/nigerias-swipe-raises-500k-pre-seed-to-expand-access-to-credit-services/" class="wpp-post-title" target="_self">Nigeria’s Swipe raises $500k pre-seed to expand access to credit services</a></h6>
</div>
</li>
</ul>
</li>
<li id="mailerlite_widget-4" class="widget widget_mailerlite_widget">
<div id="mailerlite-form_2" data-temp-id="62ee26d1d713b">
<div class="mailerlite-form">
<form action="" method="post">
<div class="mailerlite-form-title"><h3>Newsletter signup</h3></div>
<div class="mailerlite-form-description"><p>Sign up for our Newsletter</p>
</div>
<div class="mailerlite-form-inputs">
<div class="mailerlite-form-field">
<label for="mailerlite-2-field-email">Email</label>
<input id="mailerlite-2-field-email" type="email" required="required" name="form_fields[email]" placeholder="Email" />
</div>
<div class="mailerlite-form-field">
<label for="mailerlite-2-field-name">Name</label>
<input id="mailerlite-2-field-name" type="text" required="required" name="form_fields[name]" placeholder="Name" />
</div>
<div class="mailerlite-form-loader">Working.........</div>
<div class="mailerlite-subscribe-button-container">
<input class="mailerlite-subscribe-submit" type="submit" value="Subscribe" />
</div>
<input type="hidden" name="form_id" value="2" />
<input type="hidden" name="action" value="mailerlite_subscribe_form" />
<input type="hidden" name="ml_nonce" value="22891a5565" />
</div>
<div class="mailerlite-form-response">
<h4><p><span style="color: #339966;">Thank you for signing up!</span></p>
</h4>
</div>
</form>
</div>
</div>
<script type="text/javascript">
                window.addEventListener("load", function () {
                    var jQuery = window.jQueryWP || window.jQuery;

                    jQuery(document).ready(function () {

                        if(jQuery) {
                            var form_container = jQuery("#mailerlite-form_2[data-temp-id=62ee26d1d713b] form");

                            jQuery(".mailerlite-subscribe-submit", form_container).prop('disabled', true);

                            jQuery.post('https://disrupt-africa.com/wp-admin/admin-ajax.php', { "action" : "ml_create_nonce", "ml_nonce" : jQuery("input[name='ml_nonce']", form_container).val() }, function (response) {

                                if(response.success) {
                                    jQuery("input[name='ml_nonce']", form_container).val(response.data.ml_nonce);
                                    jQuery(".mailerlite-subscribe-submit", form_container).prop('disabled', false);
                                }
                            });

                            if ( typeof form_container.validate == 'function' ) {
                                form_container.submit(function (e) {
                                    e.preventDefault();
                                }).validate({
                                    submitHandler: function (form) {

                                        jQuery(this.submitButton).prop('disabled', true);

                                        form_container.find('.mailerlite-subscribe-button-container').fadeOut(function () {
                                            form_container.find('.mailerlite-form-loader').fadeIn()
                                        });

                                        var data = jQuery(form).serialize();

                                        jQuery.post('https://disrupt-africa.com/wp-admin/admin-ajax.php', data, function () {
                                            form_container.find('.mailerlite-form-inputs').fadeOut(function () {
                                                form_container.find('.mailerlite-form-response').fadeIn()
                                            });
                                        });
                                    }
                                });
                            }
                        }
                    });
                }, false);
            </script>
</li>
<li id="custom_html-2" class="widget_text widget widget_custom_html"><h3 class="widgettitle">Downloads</h3><div class="textwidget custom-html-widget"><div class="sdm_fancy2_item "><div class="sdm_fancy2_wrapper"><div class="sdm_fancy2_download_item_top"><div class="sdm_fancy2_download_thumbnail"><img class="sdm_fancy2_thumb_image" src="https://disrupt-africa.com/wp-content/uploads/2022/07/Case-Study-Alitheia-Capital.png" /></div></div><div class="sdm_fancy2_download_title">Diversity dividend: Female fund managers in Africa – Alitheia Capital</div><div class="sdm_fancy2_download_link"><a href="https://disrupt-africa.com/?smd_process_download=1&download_id=29834" class="sdm_fancy2_download_dl_link" target="_blank" rel="noopener">Download for free</a></div></div></div><div class="sdm_clear_float"></div>
<hr>
<div class="sdm_fancy2_item "><div class="sdm_fancy2_wrapper"><div class="sdm_fancy2_download_item_top"><div class="sdm_fancy2_download_thumbnail"><img class="sdm_fancy2_thumb_image" src="https://disrupt-africa.com/wp-content/uploads/2022/07/Case-Study-TLCom.png" /></div></div><div class="sdm_fancy2_download_title">Diversity dividend: Female fund managers in Africa &#8211; The TLcom Ladies</div><div class="sdm_fancy2_download_link"><a href="https://disrupt-africa.com/?smd_process_download=1&download_id=29794" class="sdm_fancy2_download_dl_link" target="_blank" rel="noopener">Download for free</a></div></div></div><div class="sdm_clear_float"></div></div></li>
</ul>
</div>
</aside>
</div> 
</div> 
<footer class="main-footer">
<div class="lower-foot">
<div class="wrap">
<div class="widgets">
<div class="textwidget"><p>Copyright © 2014-2022 Disrupt Africa. All rights reserved.</p>
</div>
<div class="menu-footer-container"><ul id="menu-footer" class="menu"><li id="menu-item-2186" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2186"><a href="https://disrupt-africa.com/about/">About</a></li>
<li id="menu-item-2491" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2491"><a href="https://disrupt-africa.com/contact/">Contact</a></li>
<li id="menu-item-2189" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2189"><a href="https://disrupt-africa.com/advertise/">Advertise</a></li>
<li id="menu-item-2279" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2279"><a href="https://disrupt-africa.com/sitemap/">Sitemap</a></li>
</ul></div> </div>
</div>
</div>
</footer>
</div> 
<script>
          if(jQuery('.prominent').next().children().length === 0){
			  jQuery('.prominent').hide()
		  };
        </script>
<link rel='stylesheet' id='sdm_addons_listing-css' href='https://disrupt-africa.com/wp-content/plugins/simple-download-monitor/includes/templates/fancy2/sdm-fancy-2-styles.css?ver=3.9.15' type='text/css' media='all' />
<script type='text/javascript' src='https://disrupt-africa.com/wp-includes/js/dist/vendor/regenerator-runtime.min.js?ver=0.13.9' id='regenerator-runtime-js'></script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=3.15.0' id='wp-polyfill-js'></script>
<script type='text/javascript' id='contact-form-7-js-extra'>
/* <![CDATA[ */
var wpcf7 = {"api":{"root":"https:\/\/disrupt-africa.com\/wp-json\/","namespace":"contact-form-7\/v1"},"cached":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/plugins/contact-form-7/includes/js/index.js?ver=5.6.1' id='contact-form-7-js'></script>
<script type='text/javascript' id='bunyad-theme-js-extra'>
/* <![CDATA[ */
var Bunyad = {"ajaxurl":"https:\/\/disrupt-africa.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
</script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/themes/smart-mag/js/bunyad-theme.js?ver=3.4.0' id='bunyad-theme-js'></script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/themes/smart-mag/js/jquery.flexslider-min.js?ver=3.4.0' id='flex-slider-js'></script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/themes/smart-mag/js/jquery.sticky-sidebar.min.js?ver=3.4.0' id='sticky-sidebar-js'></script>
<script type='text/javascript' src='https://disrupt-africa.com/wp-content/plugins/official-mailerlite-sign-up-forms/assets/js/jquery.validate.min.js?ver=6.0.1' id='jquery-validation-plugin-js'></script>
<script src='https://stats.wp.com/e-202231.js' defer></script>
<script>
	_stq = window._stq || [];
	_stq.push([ 'view', {v:'ext',j:'1:11.2',blog:'73711427',post:'0',tz:'2',srv:'disrupt-africa.com'} ]);
	_stq.push([ 'clickTrackerInit', '73711427', '0' ]);
</script>
</body>
</html>

'''

hrefs = re.findall('href="https://disrupt-africa.com/20(.+?)/">', test)
print(len(hrefs))


