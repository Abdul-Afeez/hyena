import re
valid_links = 251
if not valid_links % 50:
    print(f'Saving {valid_links % 50}')
test =['https://techpoint.africa/2021/01/01/afcfta-startups-policymakers', 'https://techpoint.africa/2022/06/28/abeg-rebrands-to-pocket', 'https://techpoint.africa/2021/06/18/nigerian-fintech-sec-regulatory-incubator', 'https://techpoint.africa/2020/10/29/oau-cu-mwas', 'https://techpoint.africa/2020/12/03/nigeria-leverage-crypto-surge', 'https://techpoint.africa/2020/10/19/paystack-exit-nigerian-startup-ecosystem', 'https://techpoint.africa/2022/06/29/begin-your-crypto-journey-with-mara-wallet', 'https://techpoint.africa/2021/05/24/2-million-mono-api-fintech', 'https://techpoint.africa/2020/09/18/path-growth-and-scale', 'https://techpoint.africa/2020/07/28/license-ngeria-nipost-logistics', 'https://techpoint.africa/2021/06/19/june-19-sexual-violence-day', 'https://techpoint.africa/2021/05/06/ethiopia-blockchain-identity-students', 'https://techpoint.africa/2020/08/17/how-i-work-ifeanyi-ndiomewes', 'https://techpoint.africa/2020/11/17/talentql-raises-300k-pre-seed-zedcrest-capital', 'https://techpoint.africa/2020/07/31/social-media-vs-news-media', 'https://techpoint.africa/2021/01/12/sec-regulate-chaka-bamboo', 'https://techpoint.africa/2021/03/16/africa-accept-paypal-via-flutterwave', 'https://techpoint.africa/2021/05/27/kenya-outlaws-pornography', 'https://techpoint.africa/2020/10/12/endpolicebrutality-nigerian-youth-make-5for5-demands-of-the-government', 'https://techpoint.africa/2021/07/14/spazio-ideale-startup-feature', 'https://techpoint.africa/2020/08/26/african-startups-yc-summer-2020-batch', 'https://techpoint.africa/2021/05/06/paystack-launches-south-africa', 'https://techpoint.africa/2021/07/15/how-microtraction-invests', 'https://techpoint.africa/2020/08/20/challenges-ecommerce-logistics-nigeria', 'https://techpoint.africa/2020/10/12/evolve-credit-feature', 'https://techpoint.africa/2020/07/27/apollo-agriculture-feature', 'https://techpoint.africa/2020/07/20/remote-work-post-lockdown', 'https://techpoint.africa/2021/02/23/spotify-nigeria-africa', 'https://techpoint.africa/2021/07/13/mkopa-appoints-duroshola-general-manager', 'https://techpoint.africa/2021/01/19/ulesson-raises-7-5m-series-a', 'https://techpoint.africa/2021/10/21/techpoint-awards-2021', 'https://techpoint.africa/2020/09/16/sec-amends-crowdfunding-regulations', 'https://techpoint.africa/2021/01/11/african-startups-raised-1-3b-briter-bridges', 'https://techpoint.africa/2020/09/17/blockchain-tool-africans-build', 'https://techpoint.africa/2021/05/24/south-afria-future-tech-ecosystem', 'https://techpoint.africa/2021/05/05/ncc-5g-connectivity-nigeria', 'https://techpoint.africa/2020/12/02/us-uk-visa-policies-tech', 'https://techpoint.africa/2022/06/30/ugochukwu-aronu-blockchain', 'https://techpoint.africa/2020/11/17/why-safeboda-leaves-kenya', 'https://techpoint.africa/2021/05/26/nigerian-startup-cribmd-2-6m-seed', 'https://techpoint.africa/2021/07/20/nigeria-mobile-money', 'https://techpoint.africa/2021/02/21/get-the-needed-help-in-a-few-clicks-make-your-life-easier-and-get-the-paper', 'https://techpoint.africa/2020/10/29/pickmeup-raises-10k-expansion', 'https://techpoint.africa/2022/01/27/nigerias-space-ambitions-pipe-dream', 'https://techpoint.africa/2021/05/05/attracting-talents-fintech-nigeria', 'https://techpoint.africa/2020/11/26/foreign-investments-nigeria-startup', 'https://techpoint.africa/2021/05/05/flextock-3-25m-pre-seed-raise', 'https://techpoint.africa/2020/09/16/using-technology-to-tell-stories-a-discussion-with-joel-kachi-benson', 'https://techpoint.africa/2021/05/08/spacex-licences-starlink-nigeria', 'https://techpoint.africa/2021/01/22/exciting-use-cryptocurrency-africa', 'https://techpoint.africa/2021/03/15/techpoint-digital-currency-summit', 'https://techpoint.africa/2020/07/28/whatsapp-multiple-devices', 'https://techpoint.africa/2021/01/06/nigerians-traded-more-than-400m-worth-crypto-2020', 'https://techpoint.africa/2021/02/19/techpoint-startup-school-port-harcourt', 'https://techpoint.africa/2020/10/28/only-10-of-female-founded-startups-in-west-africa-have-raised-up-to-1-million-since-2010', 'https://techpoint.africa/2020/07/29/itiki-agritech-startup', 'https://techpoint.africa/2020/09/14/eworker-senior-talent-feature', 'https://techpoint.africa/2021/11/30/getting-started-with-nfts', 'https://techpoint.africa/2020/12/31/memorable-nigerian-tech-moments-2020', 'https://techpoint.africa/2020/10/15/endsars-nigerian-governments-strongarm-tactics-could-drive-massive-crypto-adoption', 'https://techpoint.africa/2020/11/30/how-i-work-musty-mustapha', 'https://techpoint.africa/2020/07/20/giraffe-unicef-innovation-fund', 'https://techpoint.africa/2021/03/16/smartphone-photography-versus-digital-camera', 'https://techpoint.africa/2020/10/22/youtube-arise-news', 'https://techpoint.africa/2020/12/04/tstv-relaunch-two-months', 'https://techpoint.africa/2020/10/30/seamlesshr-raises-seven-figure-round', 'https://techpoint.africa/2021/08/03/experts-enaira-cbdc', 'https://techpoint.africa/2020/11/17/wallets-africa-partners-visa-issue-cards', 'https://techpoint.africa/2020/09/14/autochek-acquires-cheki-ghana-nigeria', 'https://techpoint.africa/2021/07/15/aifluence-raises-1m-seed', 'https://techpoint.africa/2021/01/04/nimc-mobile-app-upgraded', 'https://techpoint.africa/2020/10/28/revolutionise-nigerias-microfinance-insurtech', 'https://techpoint.africa/2020/10/19/how-i-work-ire-aderinokun', 'https://techpoint.africa/2020/10/29/cchub-acquires-kenya-elimu', 'https://techpoint.africa/2021/05/07/policy-nigerian-startups-ict-contracts', 'https://techpoint.africa/2021/01/18/nigerian-freelance-startup-terawork', 'https://techpoint.africa/2021/01/03/bitsika-2020-numbers', 'https://techpoint.africa/2020/11/16/how-i-work-uzoma-dozie', 'https://techpoint.africa/2021/01/07/fintech-predictions-2021', 'https://techpoint.africa/2020/10/20/good-bad-policies-innovation', 'https://techpoint.africa/2020/12/01/chidi-ajaere-policies-youth-changes', 'https://techpoint.africa/2021/01/05/9-policies-nigerias-tech-2020', 'https://techpoint.africa/2020/10/20/endsars-brand-engagement', 'https://techpoint.africa/2020/08/26/techpoint-build-2020-agenda', 'https://techpoint.africa/2022/06/27/over-250000000-global-users-have-chosen-the-redmi-note-series-%ef%bf%bc', 'https://techpoint.africa/2020/09/15/trump-dfc-investment-play-africa', 'https://techpoint.africa/2020/08/03/precious-mogoli', 'https://techpoint.africa/2020/10/26/bayo-adedeji-wakanow-story', 'https://techpoint.africa/2021/02/16/what-you-need-to-know-as-nigerias-lawmakers-plan-to-disqualify-journalists-without-media-degrees', 'https://techpoint.africa/2020/09/16/whatsapp-web-new-features', 'https://techpoint.africa/2021/03/17/conversation-laurin-hainey-fairmoney-ceo', 'https://techpoint.africa/2021/05/24/flat6labs-raises-10-million', 'https://techpoint.africa/2021/01/12/teamapt-business-model-west-and-north-africa', 'https://techpoint.africa/2020/07/20/telecom-160km-fibre-ekiti', 'https://techpoint.africa/2020/07/23/nigerian-telecom-financials-ncc', 'https://techpoint.africa/2020/10/06/cryptocurrency-regulation-nigeria-industry-players', 'https://techpoint.africa/2020/10/27/millionaire-west-african-startups-shutdown', 'https://techpoint.africa/2021/05/24/safaricom-ethiopia-licence', 'https://techpoint.africa/2020/11/30/lagos-executive-unified-fibre-project', 'https://techpoint.africa/2021/01/08/covid-vaccines-africa-tech-solutions', 'https://techpoint.africa/2021/02/22/nigerias-healthtech-startup-funding-grew-404-ecommerce-almost-hit-5900-in-2020', 'https://techpoint.africa/2020/11/18/startup-funding-tallp', 'https://techpoint.africa/2020/07/20/how-i-work-from-home-tage-kene-okafor-techpoint-africa-startup-reporter', 'https://techpoint.africa/2020/11/30/inside-agritech-conglomerate-farmcrowdy-building', 'https://techpoint.africa/2020/08/10/how-i-work-yinka-awosanya', 'https://techpoint.africa/2022/04/06/techpoint-africa-296', 'https://techpoint.africa/2022/02/08/why-are-artistes-interested-in-african-startups', 'https://techpoint.africa/2021/01/20/etop-ikpe-interview', 'https://techpoint.africa/2020/12/11/lady-buckit-nollywood-animation-movie', 'https://techpoint.africa/2020/10/27/nigerias-broadcast-regulator-journalism', 'https://techpoint.africa/2021/01/11/whatsapp-policy-update-africa', 'https://techpoint.africa/2020/10/12/endsars-2020-movement', 'https://techpoint.africa/2021/01/14/uganda-social-media-shutdown-2021', 'https://techpoint.africa/2020/09/14/sec-nigeria-regulations-cryptocurrency', 'https://techpoint.africa/2020/07/20/e4e-launch', 'https://techpoint.africa/2020/07/21/inside-nigerias-digital-identification', 'https://techpoint.africa/2021/02/22/nigeria-lost-5b-fraud-2020', 'https://techpoint.africa/2020/12/04/nigerian-online-grocery-store-inflation', 'https://techpoint.africa/2020/08/21/cryptocurrency-adoption-nigeria', 'https://techpoint.africa/2021/10/21/what-does-the-african-fintech-need', 'https://techpoint.africa/2020/10/30/mtn-group-sells-stake-jumia', 'https://techpoint.africa/2020/11/17/nigeria-adopt-blockchain-2030', 'https://techpoint.africa/2020/10/27/paystack-acquisition-policy-nigeria', 'https://techpoint.africa/2021/08/03/payhippo-enters-y-combinator', 'https://techpoint.africa/2021/06/12/blockchain-nigeria-elections', 'https://techpoint.africa/2020/11/27/nigeria-dominance-west-africa', 'https://techpoint.africa/2020/10/12/local-partners-support-facebook', 'https://techpoint.africa/2021/05/25/egyptian-agritech-mozare3-1million-raise', 'https://techpoint.africa/2020/10/29/nigeria-network-national-roaming', 'https://techpoint.africa/2020/08/04/nigerias-banks-debit-loan-defaulters', 'https://techpoint.africa/2020/09/18/nigeria-account-self-certification', 'https://techpoint.africa/2020/07/24/consumer-protection-tech', 'https://techpoint.africa/2021/05/07/twitter-tip-jar', 'https://techpoint.africa/2021/05/06/google-hybrid-future-remote-work', 'https://techpoint.africa/2020/09/16/cama-2020-what-benefits-for-startups-and-msmes', 'https://techpoint.africa/2020/10/15/endsars-bypass-internet-shutdown-nigeria', 'https://techpoint.africa/2021/03/16/nigerians-pay-ussd-banking-service', 'https://techpoint.africa/2020/09/18/facebook-lagos-office', 'https://techpoint.africa/2021/07/19/chaka-raises-pre-seed', 'https://techpoint.africa/2020/07/22/data-privacy-online-advertising', 'https://techpoint.africa/2020/10/28/oui-capital-feature', 'https://techpoint.africa/2020/07/21/internet-fibre-northern-nigeria', 'https://techpoint.africa/2021/05/05/nigeria-crypto-trading-lead-transaction', 'https://techpoint.africa/2020/11/24/afrikrea-online-infrastructure-african-culture-commerce', 'https://techpoint.africa/2020/07/17/nigerian-companies-global-cyberattacks', 'https://techpoint.africa/2020/11/27/do-more-founders-startup-mean-more-investments', 'https://techpoint.africa/2021/10/25/support-techpoint-africa', 'https://techpoint.africa/2020/08/05/techpoint-build-2020-speakers', 'https://techpoint.africa/2021/01/08/tokunbo-adetona-leads-nairabox-jay-chikezie-steps-down-co-ceo', 'https://techpoint.africa/2020/07/30/kiakiaprint-going-global-with-canva-partnership-and-sa-expansion', 'https://techpoint.africa/2021/07/15/pos-business-in-nigeria', 'https://techpoint.africa/2020/09/15/sec-cryptocurrency-statement', 'https://techpoint.africa/2021/03/10/speakers-digital-currency-summit-2021', 'https://techpoint.africa/2022/06/29/ayobamigbe-teriba-founders-factory-africa', 'https://techpoint.africa/2020/08/24/how-future-hub-invests', 'https://techpoint.africa/2021/03/12/netflix-restrict-password-sharing', 'https://techpoint.africa/2020/12/13/disney-kugali-media-animated', 'https://techpoint.africa/2020/08/25/kenya-public-primary-schools-internet', 'https://techpoint.africa/2021/02/22/nigeria-nin-74k-covid-19', 'https://techpoint.africa/2021/02/17/twitter-african-gig-economy', 'https://techpoint.africa/2020/09/15/africa-gig-economy', 'https://techpoint.africa/2020/12/02/nigerian-fintech-startup-credpal-raises-1-5m', 'https://techpoint.africa/2020/10/15/paystack-acquired-by-stripe', 'https://techpoint.africa/2020/07/27/hiw-emmanuel-paul', 'https://techpoint.africa/2020/07/31/ghana-digital-elections-pandemic', 'https://techpoint.africa/2020/07/20/kenya-regulate-digital-lenders', 'https://techpoint.africa/2021/05/26/insurance-sales-agent-questionnaire', 'https://techpoint.africa/2021/03/16/enable-pay-with-paypal-flutterwave', 'https://techpoint.africa/2020/07/30/airtel-africa-q2-2020', 'https://techpoint.africa/2020/10/21/service-disruption-mtn-lekki', 'https://techpoint.africa/2020/09/18/social-dilemma-social-media-africa', 'https://techpoint.africa/2022/06/28/selina-onyando-tech-policy-expert', 'https://techpoint.africa/2021/05/26/enye-startup-feature', 'https://techpoint.africa/2020/08/25/nigerian-states-rewards-row-charges', 'https://techpoint.africa/2022/06/29/cloud-kitchens-kunes-kenya', 'https://techpoint.africa/2021/06/18/babajide-duroshola-safeboda', 'https://techpoint.africa/2020/08/03/nigerian-startups-q2-2020', 'https://techpoint.africa/2022/03/25/quidax-unveils-don-jazzy-as-its-brand-ambassador', 'https://techpoint.africa/2020/10/29/airtel-to-exit-ghana-operations-as-government-prepares-takeover', 'https://techpoint.africa/2020/08/26/worldremit-acquires-sendwave-500m', 'https://techpoint.africa/2020/08/24/how-i-work-samuel-okike', 'https://techpoint.africa/2020/07/21/valr-raises-3-4m', 'https://techpoint.africa/2020/12/31/techpoint-africa-six-years-old', 'https://techpoint.africa/2021/01/21/when-companies-die', 'https://techpoint.africa/2021/01/19/nigerian-tech-policies-2021', 'https://techpoint.africa/2021/01/04/how-greenhouse-capital-invests', 'https://techpoint.africa/2021/05/06/gozem-ride-hailing-gabon', 'https://techpoint.africa/2022/06/29/confirmed-speakers-termii-elevate', 'https://techpoint.africa/2020/10/22/facebook-lekkimassacre-false', 'https://techpoint.africa/2020/08/24/employees-interest-nigerian-tech-space', 'https://techpoint.africa/2020/10/09/netflix-africa-mobile-only-plan', 'https://techpoint.africa/2020/12/29/nigeria-biggest-hashtags-2020', 'https://techpoint.africa/2020/08/03/dele-odufuye-flobyt-traffic-talk-silent-acquisition-tsaboin', 'https://techpoint.africa/2020/11/24/asuu-rejects-ippis-suggests-utas', 'https://techpoint.africa/2020/12/02/francophone-africa-tech-players-breaking-down-barriers-recognition', 'https://techpoint.africa/2021/03/14/ussd-nigeria-stops-march-15-2021', 'https://techpoint.africa/2020/10/14/flutterwave-denies-cbn-questioning-bitcoin-surges', 'https://techpoint.africa/2021/03/23/twitter-undo-tweet-feature', 'https://techpoint.africa/2021/02/23/nigerian-bus-hailing-platform-hubryde', 'https://techpoint.africa/2021/01/15/whatsapp-business-privacy-dilemma']
print(len(test))
