#http://bit.ly/mousey-qa
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return """

    <DOCTYPE! html>

    <head>

        <style>

            body {

                background-color: #000000;

                color: #FFFFFF;

                font-size: 2.62em;

                }



            p , ul , ol , h1 , h2 , h3 , h3 , h4 , h5 , h6   {

                color: #1aff1a;

                text-align: center;

                margin: 2px auto;

                }

            a {

                text-align: center;

                color: #00FFFF;

            }

            a.nn-page {

                color: yellow;

            }


            p.ylloh , h1.ylloh , h2.ylloh , h3.ylloh , h3.ylloh , h5.ylloh , h6.ylloh {

                color: yellow;

                margin: 2px auto;

                }

            p.def , p.ex {

                font-style: italic;

            }

            # p.ex for examples &/or explanations

            div.purple-line-thing {

                border-bottom: 3px dotted purple;

            }

            iframe {

                display:block;

                margin:0 auto;

                border:none;

            {

        </style>

    </head>

    <body>

        <h4> <i> a work in progress </i> </h4>

        <br>

        <h3>  introducing ...  </h3>

        <br>

        <h1 class="ylloh" id="mousey-pals">  Mousey-Qa & Pals  </h1>

        <br>

        <h2> most recent episode ( thanks { or ' thaenx ' } SoundCloud ! ) : </h2>

        <br>

        <p> more and different thaengz <a href="#main">below</a> </p>

        <br>

        <p id="thaeng" class="def"> thaeng(z) - includes conceptualizations ,&nbsp;<a href="/#een">ee'n</a>* thing(s) ( physical phenomena ) </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/soundcloud%253Atracks%253A2294230349&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"> </iframe> <div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"> <a href="https://soundcloud.com/drucey-710670561" title="Drucey" target="_blank" style="color: #cccccc; text-decoration: none;">Drucey</a> · <a href="https://soundcloud.com/drucey-710670561/out-of-the-park-and-towards-it" title="Out Of The Park And Towards It - March 31, 2026 at 2:54 PM" target="_blank" style="color: #cccccc; text-decoration: none;">Out Of The Park And Towards It - March 31, 2026 at 2:54 PM</a> </div>

        <br>

        <h4> related-to-episode musings : <a href="#main">( or main menu )</a> </h4>

        <br>

        <p> we are beyond  <a href="/#een">ee'n</a>* notions "lovers" , "students" ,... </p>

        <br>

        <p> ... we're <a href="/ancient-truths">multi-capable</a> ( planning , sensing , acting , communicating , <i>etc.</i> ) ... </p>

        <br>

        <p> { essentially : able === " I can ! " ; capable === " <i>this</i> able " } </p>

        <br>

        <p> ... we commonly experience life differently ( <a target="_blank" href="https://dictionary.cambridge.org/us/dictionary/english/aka">AKA</a> <a href="https://www.merriam-webster.com/dictionary/sonder">sonder</a> ) ... </p>

        <br>

        <p> ... we are all family ... <a href="https://en.wikipedia.org/wiki/Ubuntu_philosophy">ubuntu</a> ... </p>

        <br>

        <p> ... <a href="/#namaste">namaste</a> ! </p>

        <br>
        <div class="purple-line-thing"> </div>

        <br>

        <h3> episode : <a href="https://soundcloud.com/drucey-710670561/priscilla-weighs-in-on?si=3521c8ee7eef4792b93da63b6939ac16&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing">Priscilla Weighs In</a> </h3>

        <br>

        <h4 id="emo-types"> episode elucidation - feeling  types ( emotions & sensations ) : </h4>

        <br>

        <p class="ylloh"> <u> <i> positive / yearnible types (2) : </i> </u> </p>

        <br>

        <ul>

            <li>

                <p> glad | gladly &nbsp;&nbsp; :: &nbsp;&nbsp; joyous | happy | pleased | satisfied | contented </p>

                <br>

                <p class="ex"> example - " I feel glad that you said that " </p>

            </li>

                <br>

            <li>

                <p> " rad " | radly &nbsp;&nbsp; :: &nbsp;&nbsp; amazed | wowed | delighted | ecstatic | excited </p>

                <br>

                <p class="ex"> example - " what a rad basketball play ! " </p>

            </li>

        </ul>

        <br>

        <p class="ylloh"> <u> <i> but yet perhaps these unwanted types (3) also : </i> </u> </p>

        <br>

        <ul>

            <li>

                <p> sad | sadly &nbsp;&nbsp; :: &nbsp;&nbsp; mournful | grieving | "upset" | lament | dejected </p>

                <br>

                <p class="ex"> example - " I feel sadly for many animal people " </p>

            </li>

                <br>

            <li>

                <p> mad | madly &nbsp;&nbsp; :: &nbsp;&nbsp; angst | frustration | "upset" | bothered | "spaced out" </p>

                <br>

                <p class="ex"> example - " I'm mad about it ; I want change " </p>

            </li>

                <br>

            <li>

                <p> bad | badly &nbsp;&nbsp; :: &nbsp;&nbsp; regretful | despondent | guilty | ashamed | "upset" </p>

                <br>

                <p class="ex"> example - " I feel so badly about it all " </p>

            </li>

        </ul>

        <br>

        <br>

        <p> <u>additionally</u> : fearful , scared , anxious , worried , afraid </p>

        <br>

        <p> ... and (dis)comforts , (dis)pleasures , delight , disgust , nervousness , hurt(s) , <i> <a target="_blank" href="https://en.wikipedia.org/wiki/Et_cetera">etc.</a> </i> </p>

        <br>

        <p> to learn these with " duchee " associations : <a href="/duchee">duchee-ing</a> </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> holding an urgent question or similar concern ? </p>

        <br>

        <p> you may message this website's curator-creator ... </p>

        <br>

        <p> ... via e-mail : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p id="main"> we <a target="_blank" href="https://www.merriam-webster.com/dictionary/noob">noobies</a> living in ... </p>

        <br>

        <p> ... the <a target="_blank" href="https://en.wiktionary.org/wiki/cosmos">kosmos</a> , wild & wonderful life , nature ... </p>

        <br>

        <p> ... doth profess that important , veritable truths ... </p>

        <br>

        <p class="def"> veritable - could be checked , proven , likewisely knowable </p>

        <br>

        <p> ... oughta be known surely , <i> improvingly </i> , by all ... </p>

        <br>

        <p> ... such as : </p>

        <br>

        <p> what comprises ordinarily <i> <a target="_blank" href="https://www.merriam-webster.com/dictionary/apropos">apropos</a> </i> <a target="_blank" href="#love-ways">love-ways</a> </p>

        <br>

        <p> the ( five | 5 ) main <a target="_blank" href="#cat-love">categories of love</a> </p>

        <br>

        <p> how to , <i> <a target="_blank" href="https://en.wiktionary.org/wiki/en_g%C3%A9n%C3%A9ral">en générale</a> </i> , <a target="_blank" href="/#NVC">communicate compassionately</a> , effectively </p>

        <br>

        <p> the ( five | 5 ) main types of emotions ( <a target="_blank" href="#emo-types">above</a> ) ... </p>

        <br>

        <p> ... the ( ten | 10 ) aspects of enjoyable , sustainable living </p>

        <br>

        <p> ( <a target="_blank" href="#five-f">'the five Fs '</a> & <a target="_blank" href="#five-r">'the five Rs '</a> ) </p>

        <br>

        <p> ... the ( five | 5 ) <a target="_blank" href="#needs">common needs</a> </p>

        <br>

        <p> ... how to " duchee " ( positively correlate quantitatively ) : <a href="/duchee">duchee-ing</a> </p>

        <br>

        <p id="Ilesk-main"> ... a new language project entitled <a href="/Ilesk">" Ilesk "</a> </p>

        <br>

        <p> ... supportive <a target="_blank" href="/#reco">recommendations</a> ... </p>

        <br>

        <p> ... and inspirational quotes along the way ... </p>

        <br>

        <div class="purple-line-thing"> </div>

        <p> <i> immediately aforesaid <a href="/#thaeng">thaengzs</a> proceedeth : </i> </p>

        <div class="purple-line-thing"> </div>

        <br>

        <h2 class="ylloh" id="love-ways"> ordinary love-ways ( exemplary videos ) ( <a target="_blank" href="https://en.wikipedia.org/wiki/The_Five_Love_Languages">" The Five Love Languages "</a> ) : <a href="#main"> <i>main menu</i> </a> </h2>

        <br>

        <p>  acts of service  - getting garlic for your <a target="_blank" href="https://youtu.be/oKv4a10USpw">roommate</a> </p>

        <br>

        <p>  special time  - such as with <a target="_blank" href="https://youtu.be/KydI7KF3YkM">koala youth</a> </p>

        <br>

        <p>  words of praise  - <a target="_blank" href="https://youtu.be/MlBmnFxCYdo"> <i>like this</i> </a> </p>

        <br>

        <p>  gifting & receiving  - <a target="_blank" href="https://youtu.be/CdJWaEZundk">like " couple boba keychains "</a> </p>

        <br>

        <p>  quite nice intimacy  - <a target="_blank" href="https://youtu.be/t52DEpkNMGg">similar to these hugs</a> </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <h2 class="ylloh" id="five-f"> requisite aspects of enjoyable living : <a href="#main"> <i>main menu</i> </a> </h2>

        <br>

        <p> ' the 5 Fs ' : faith ; friendship ; fitness ; fructivity ; fun </p>

        <br>

        <p> ' the 5 Rs ' : "ratcheting" , reuse ; repair ; replenishment ; renewing </p>

        <br>

        <br>

        <h3 class="ylloh" id="faith"> <u> trust & faith </u> </h3>

        <br>

        <p> " every great dream begins with a dreamer ; </p>

        <br>

        <p> always remember , you have within you the </p>

        <br>

        <p> strength , the patience , and the passion to </p>

        <br>

        <p> reach for the stars , to change the world " </p>

        <br>

        <p> <i> — Harriet Tubman ( of <a target="_blank" href="https://en.wikipedia.org/wiki/Underground_Railroad">" the Underground Railroad "</a>) </i> </p>

        <br>

        <br>

        <p> faith , trust , must include and rely upon ... </p>

        <br>

        <p id="yeshu"> " Christ Immanuel " <a target="_blank" href="https://dictionary.cambridge.org/us/dictionary/english/aka">AKA</a> " Yeshu " of ' Ga ' </p>

        <br>

        <p> we can pray to Him for <a href="/#thaeng">anythaeng</a> </p>

        <br>

        <p> ' Ga ' is pronounced like and same as ... </p>

        <br>

        <p> ... "g" in <a target="_blank" href="https://en.wikipedia.org/wiki/Names_of_God"> <u>G</u>od</a> & "ah" in <a target="_blank" href="https://simple.wikipedia.org/wiki/Allah">All<u>ah</u> </a> </p>

        <br>

        <p> " Yeshu " is pronounced like "ye" in yes ... </p>

        <br>

        <p> ... and "shu" like in shoe </p>

        <br>

        <p> ( relatedly : <a target="_blank" id="namaste" href="https://en.wikipedia.org/wiki/Namaste">Namaste</a> / <a target="_blank" href="https://en.wikipedia.org/wiki/Takbir">Takbir!</a> / <a target="_blank" href="https://en.wikipedia.org/wiki/Great_Spirit">Great Spirit</a> / <a target="_blank" href="https://en.wikipedia.org/wiki/Shalom">Shalom</a> / <i> etc. </i> ) </p>

        <br>

        <p> in practice , whether prayer , contemplation , or meditation </p>

        <br>

        <p> if inviting and heeding Him ... 'tis <a target="_blank" href="https://en.wikipedia.org/wiki/Legit">"legit"</a> </p>

        <br>

        <br>

        <p> <i> could you make a heartfelt prayer now ? </i> </p>

        <br>

        <br>

        <p> heartfelt - elicits , stirs inimicably good feelings </p>

        <br>

        <p> elicit - " draw forth " , to somehow safely cause  </p>

        <br>

        <p> inimicable - quite implausible to replicate nefariously </p>

        <br>

        <p> implausible - impossible , but referring to bad <a href="/#thaeng">thaengzs</a> </p>

        <br>

        <p> nefarious - wicked or criminal , perhaps sophisticatedly so </p>

        <br>

        <p> sophisticated - coherent , cogent , complex , could  <a href="/#een">ee'n</a>* help </p>

        <br>

        <p> prayer - a request to , conversation with <a href="/#yeshu">Yeshu</a> </p>

        <br>

        <br>

        <p> <i> could you meditate or contemplate piously soon ? </i> </p>

        <br>

        <br>

        <p> meditation - beneficial practice of noetic stillness </p>

        <br>

        <p id="noetic"> noetic - of mind(s) ; ordinary , extraordinary psychic phenomena </p>

        <br>

        <p> contemplation - alike to meditation , includes critical thinking </p>

        <br>

        <p id="pious"> piously - humbly and devoutly ,  <a href="/#een">ee'n</a>* penitently </p>

        <br>

        <p> humble - aware of ( personal ) limitations , constraints , impossibilities

        <p> <i> { safe to achieve via prayerfulness with Yeshu } </i> </p>

        <br>

        <p> devout - earnestly striving for , dedicated to goodness </p>

        <br>

        <p id="een"> * ee'n - replacing "even" insofar as " perhaps also " ... </p>

        <br>

        <p> ... but not for these numbers : 2 , 4 , <i> <a target="_blank" href="https://en.wikipedia.org/wiki/Et_cetera">etc.</a> </i> </p>

        <br>

        <p> penitent - acknowledging one's culpability and repenting , amending </p>

        <br>

        <br>

        <h3 class="ylloh"> <u> play & fun </u> </h3>

        <br>

        <br>

        <p> “ when life throws you a rainy day , </p>

        <br>

        <p> play in the puddles ” <i> — from <a target="_blank" href="https://en.wikipedia.org/wiki/Winnie-the-Pooh">"Winnie-the-Pooh"</a> </i> </p>

        <br>

        <br>

        <p> recreation , wild wondering , safely adventuring </p>

        <br>

        <p> reusing what maybe seemed wasted </p>

        <br>

        <p> such is requisite for continued goodness , love </p>

        <br>

        <p> <a target="_blank" href="https://soundcloud.com/drucey-710670561/penny-p-knows-it-safely-march">Penny-P Knows It Safely</a> </p>

        <br>

        <p> <i> could you play courageously yet conscientiously soon ? </i> </p>

        <br>

        <p> examples : art-making , nature exploration , library learning </p>

        <br>

        <br>

        <h3 class="ylloh"> <u> teamwork & friendships </u> </h3>

        <br>

        <p> teams , partnerships , friendships endure via invitation , agreement </p>

        <br>

        <p> agreements oughta be based upon veritable concurrence(s) </p>

        <br>

        <p> <i> concurrence - prayerfully accepted discernment , knowledge , information , etc. </i> </p>

        <br>

        <p> agreements could be adjusted and issues resolved </p>

        <br>

        <p> but merely , haughtily expecting obeisance fails us </p>

        <br>

        <p id="jesus"> teamwork ought also include " Yeshu " ( Jesus Christ ) ... </p>

        <br>

        <p> ... ( perhaps discretely ) for best results and safe fun </p>

        <br>

        <br>

        <p> <i> could you co-create a fun-to-keep agreement sometime ? </i> </p>

        <br>

        <p> { only invitation , offering , asking , requests are ethical } </p>

        <br>

        <br>

        <p> " friendship is like wetting your pants </p>

        <br>

        <p> everyone can see it but only you can </p>

        <br>

        <p> feel its true warmth " </i> — anonymous </i> </p>

        <br>

        <br>

        <h3 class="ylloh"> <u> "shape" & fitness </u> </h3>

        <br>

        <p> <a target="_blank" href="https://www.spanishdict.com/translate/exercise">ejercisio</a> : " fun zone " , eustress , and ' E-Z ' </p>

        <br>

        <p> <i> " fun zone " - eliciting enjoyed efforts </i> </p>

        <br>

        <p> <i> eustress - beneficial duress if exerting with Yeshu </i> </p>

        <br>

        <p> <i> ' E-Z ' - excellence and zeal , perhaps sometimes easily </i> </p>

        <br>

        <br>

        <p> " fitness is not a destination , </p>

        <br>

        <p> it's a way of life " </p>

        <br>

        <br>

        <p> <i> could you enjoy fresh fun , frolicking play ? </i> </p>

        <br>

        <br>

        <p> nutrition : prayerfully checked via smell , other senses </p>

        <br>

        <br>

        <p> <i> could you consume only vegetarian , vegan meals ? </i> </p>

        <br>

        <p> ( we do ! ) </p>

        <br>

        <br>

        <p> " just for today " { and mayhaps tomorrows } — "J.G." </p>

        <br>

        <br>

        <h3 class="ylloh"> <u> contribution & fructivity </u> </h3>

        <br>

        <p> pious progress has potential for consistent contribution </p>

        <br>

        <p> yet private practice isn't a concert performance ! </p>

        <br>

        <p> somehow recording our progress keeps us honest </p>

        <br>

        <p> creativity aids critical thinking ; reversed also true </p>

        <br>

        <br>

        <p> " what gets measured gets managed " <i> — Peter Drucker </i> </p>

        <br>

        <p> <i> could you record aspirational progress simply , succinctly ? </i> </p>

        <br>

        <p> doodling and singing a note may suffice ! </p>

        <br>

        <br>

        <p> " creativity is intelligence having fun " <i> — Albert Einstein </i> </p>

        <br>

        <p> <i> could you strive to express anew creatively ? </i> </p>

        <br>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <h2 id="needs" class="ylloh"> our common needs (5) : <a href="#main"> <i>main menu</i> </a> </h2>

        <br>

        <h3> i. <u> sureties </u> - safety , sensitivity , sustenance , shelter , slumber , security </h3>

        <br>

        <p class="def"> safety - peaceful circumstance(s) lacking threat(s) , violence , insult(s) </p>

        <br>

        <p class="def" id="sensi"> sensitivity - aware for sentience , cautiously and carefully </p>

        <br>

        <p class="def"> { advice : <a href="/#sympa">sympatico</a> , <a target="_blank" href="/#sensi">above</a> ; neither sympathy nor empathy } </p>

        <br>

        <p class="def"> advice - a declaration regarding what is pyudent </p>

        <br>

        <p class="def"> pyudence - pious progress , passion , prurience , playfulness & privacy </p>

        <br>

        <p class="def"> prurience - nurturing of genuine ( prayerful ) sensuality , intimacy </p>

        <br>

        <p class="def"> sustenance - fruits , veggies , and similar ; natural waters </p>

        <br>

        <p class="def"> shelter - holistic protection from chaos , extremes , harm </p>

        <br>

        <p class="def"> slumber - rest , recuperation , sleep , relaxation </p>

        <br>

        <p class="def"> security - prescient protection of genuinely valuable belongings </p>

        <br>

        <h3> ii. <u> variety </u> - " the spice of life " , novelty & originality </h3>

        <br>

        <p class="def"> novelty - uniquely different newness ,  <a href="/#een">ee'n</a>* rarely so </p>

        <br>

        <p class="def"> originality - fructive work that is distinctly different </p>

        <br>

        <h3> iii. <u> love </u> - affinity & affection , caution & care </h3>

        <br>

        <p class="def"> affinity - an essence of friendship , fondness and appreciation </p>

        <br>

        <p class="def"> affection - showing love via such as allowed tenderness </p>

        <br>

        <p class="def"> caution - <a target="_blank" href="https://www.merriam-webster.com/dictionary/vigilant">vigilant</a> protectiveness if dangers are <a target="_blank" href="https://www.merriam-webster.com/dictionary/extant">extant</a> </p>

        <br>

        <p class="def"> care - primarily , results via heeding <a target="_blank" href="/#jesus">Yeshu</a> ( prayerfully ) </p>

        <br>

        <h3> <u> progress </u> - practice and learning , practical and pragmatic </h3>

        <br>

        <p class="def"> practical - regarding , about , physical issues , challenges , opportunities </p>

        <br>

        <p class="def"> pragmatic - regarding , about , <a target="_blank" href="/#noetic">noetic</a> issues , challenges , opportunities </p>

        <br>

        <h3> <u> contribution </u> </i> - <a target="_blank" href="https://www.merriam-webster.com/dictionary/magnum%20opus">a magnum opus</a> , culmination(s) of fructivity </h3>

        <br>

        <p class="def"> culmination - a putting together of similar efforts </p>

        <br>

        <p class="def"> fructivity - anythaeng beneficial , done for goodness , aidsome </p>

        <br>

        <p class="def"> aidsome - that which <a target="_blank" href="https://www.merriam-webster.com/dictionary/aid">aids</a> us , however much </p>

        <br>

        <br>

        <p> " all { we } need is { results of } love " </p>

        <br>

        <p> — the Beatles ( and us via brackets honoringly ) </p>

        <br>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <h2 id="cat-love" class="ylloh"> the five ancient love types ( Greek origin ) : </h2>

        <br>

        <p> <a target="_blank" href="https://soundcloud.com/drucey-710670561/agape-plus-march-25-2026-at-12">Agape Plus</a> </p>

        <br>

        <p> <u> agape </u> - altruistic love for all families ( everyone deserving ) </p>

        <br>

        <p> <u> storje </u> - dedicated , devotional love with specific application </p>

        <br>

        <p> <u> philautia </u> - s'<a target="_blank" href="https://en.wikipedia.org/wiki/Elf_(film)">elf</a> love , best kept in moderation </p>

        <br>

        <p> <u> filea </u> - the love of chosen friends , pals </p>

        <br>

        <p> <u> ludus </u> - playfulness , <a target="_blank" href="https://crazywisefilm.com/">" crazy-wise "</a>&nbsp;,  child-like spirit </p>

        <br>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <h2 class="ylloh" id="NVC"> <a target="_blank" href="https://www.cnvc.org/">compassionate communication</a> ( <a target="_blank" href="https://youtu.be/NYkgbrZSAY0?si=TUR_y0sNdQ_Zyesn">"NVC"</a> | ' Team-Talk ' ) : <a href="#main"> <i>main menu</i> </a> </h2>

        <br>

        <p> communicating very nicely ought include these ( 5 , 5 ) : </p>

        <br>

            <ul>

                <li>

        <p> <i>i.</i> each and every statement type ( <a target="_blank" href="#onistad">below</a> ) concordantly </p>

                <br>

                <p> concordance - shared understanding , wisdom , knowledge ( <a target="_blank" href="/#faith">with Yeshu</a> ) </p>

                </li>

                    <br>

                <li>

        <p> <i>ii.</i> keeping genuine sympatico aloft ( listening for yearnings ) </p>

        <br>

        <p class="def" id="sympa"> sympatico - natural accord amongst peers , partners , pals  </p>

                </li>

                    <br>

                <li>

        <p> <i>iii.</i> refraining from bad judgments ( haste makes waste ) </p>

                </li>

                    <br>

                <li>

        <p> <i>iv.</i> maintaining a respectful presence with others ( good vibes ) </p>

                </li>

                    <br>

                <li>

        <p> <i>v.</i> aware that worldviews are thoughts, emotions feelings </p>

                <br>

                <p> <i> our thoughts about reality muchly cause emotivity </i> </p>

                </li>

            </ul>

        <br>

        <p id="onistad"> <i>i.</i> <u>'onistad' honesty</u>  - humbly conveyed experiential truths , views </p>

            <br>

            <p> " these boogers appear greenish to me " </p>

            <br>

            <p> " I acknowledge this " </p>

            <br>

        <p> <i>ii.</i> <u>felt feelings</u> - actually ours ( glad , rad , "upset" ) </p>

            <br>

                    <p> " I feel so rad about the Chipmunks " </p>

                    <br>

                    <p> " yeah ! me also ! " </p>

            <br>

        <p> <i>iii.</i> <u>yay-ible yearnings</u> - needs , desires , "values" Yeshu O-Ks </p>

            <br>

                    <p> " wanna walk in the woods ? " </p>

                    <br>

                    <p> " yeah let's go ! " </p>

            <br>

        <p> <i>iv.</i> <u>respectful requests</u> - courteously asking not unkindly commanding </p>

            <br>

                    <p> " could you turn it up please ? " </p>

                    <br>

                    <p> " <a target="_blank" href="https://www.youtube.com/watch?v=6FOUqQt3Kg0"> R-E-S-P-E-C-T [...] </a> " </p>

        <br>

        <p> <i>v.</i> <u> <a target="_blank" href="https://discord.gg/7GC366jj">cheerful chat</a> </u> - for fun , relished reprieve , love </p>

            <br>

                    <p> " hey ! how are ya ? " </p>

                    <br>

                    <p> " not so bad ! and you ? " </p>

            <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <h2 class="ylloh" id="five-r"> <a target="_blank" class="nn-page" href="/five-Rs">the five Rs</a> : <a href="#main"> <i>main menu</i> </a> </h2>

        <br>

        <p> <a target="_blank" class="nn-page" href="/five-Rs">"ratcheting"</a> - purely positive , valorously vulnerable , consistently caring </p>

        <br>

        <p> <a target="_blank" class="nn-page" href="/five-Rs">replenishing</a> Gaia's natural cycles ( flora , fauna , funga ) </p>

        <br>

        <p> <a target="_blank" class="nn-page" href="/five-Rs">reusing</a> rather than only and merely disposing </p>

        <br>

        <p> <a target="_blank" class="nn-page" href="/five-Rs">refraining</a> from any waste , negligence , theft , or harm </p>

        <br>

        <p> <a target="_blank" class="nn-page" href="/five-Rs">renewing</a> our minds , emboldening our good spirits ... </p>

        <br>

        <iframe style="display:block; margin:0 auto; border:none;" width="560" height="315" src="https://www.youtube.com/embed/GyOMYC6mlsY?si=tGeVCjRH_IL3XZNa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>

        <br>

        <iframe style="display:block; margin:0 auto; border:none;" width="560" height="315" src="https://www.youtube.com/embed/OiYjTb3opAA?si=8t9EvFTvZAhfPOPd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> wanna compassionately chat with ' Mousey-Pals ' & <a target="_blank" href="https://en.wikipedia.org/wiki/Captain_Planet_and_the_Planeteers">" Planeteers "</a> ? </p>

        <br>

        <p> we are about doing our duties joyously ! </p>

        <br>

        <p> such may join our Discord server : <a target="_blank" href="https://discord.gg/7GC366jj">Pals of Mousey-Qa</a> </p>

        <br>

        <br>

        <p> to ( kindly ) message this website's curator-creator ...</p>

        <br>

        <p> ... you may e-mail "Druce" : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <p> <i> novel notions <a target="_blank" href="collinsdictionary.com/dictionary/french-english/gratuit">gratuit</a> from Aware Advisory Services </i> </p>

        <br>

        <p> big thanks to the <a target="_blank" href="https://www.pythonanywhere.com/">PythonAnywhere.com</a> internet-service team </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> * === new from " Ilesk " , a language project </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p id="#reco"> <u> <i> recommendations </u> : <a href="/#main">menu</a> </i>  </p>

        <br>

        <p> "heartwarming" reads : <a target="_blank" href="https://www.kindspring.org/">KindSpring</a> </p>

        <br>

        <p> charity : <a target="_blank" href="https://www.givedirectly.org/">GiveDirectly</a> </p>

        <br>

        <p> for good spirits , hearty laughter , potent purity : </p>

        <br>

        <p> <a target="_blank" href="https://web.archive.org/web/2/http://html5zombo.com/">ZomboCom</a> </p>

        <br>

        <p> <a target="_blank" href="https://www.youtube.com/c/mylittlepony">My Little Pony - Official Channel</a> </p>

        <br>

        <p> <a target="_blank" href="https://www.earwolf.com/episode/earwolf-presents-hello-from-the-magic-tavern/">Hello From The Magic Tavern</a> </p>

        <br>

        <p> <i> { plausibly in order of ascending requisite maturity } </i> </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

    </body>

    </html>

    """

@route('/five-Rs')

def five_Rs():

    return """

    <DOCTYPE! html>

    <head>

        <style>

        body {

                background-color: #000000;

                color: #FFFFFF;

                font-size: 2.62em;

                }

            a   {

                color: #00FFFF;

            }

            p , ul , ol , h1 , h2 , h3 , h3 , h4 , h5 , h6   {

                color: #1aff1a;

                text-align: center;

                margin: 2px auto;

                }

            p.ylloh , h1.ylloh , h2.ylloh , h3.ylloh , h3.ylloh , h5.ylloh , h6.ylloh {

                color: yellow;

                margin: 2px auto;

                }

            div.purple-line-thing {

                border-bottom: 3px dotted blue;

            }

            div.purple-line-thing {

                border-bottom: 3px dotted purple;

            }

            iframe {

                display:block;

                margin:0 auto;

                border:none;

            {

        </style>

    </head>

    <body>

        <br>

        <h1 class="ylloh" id="five-r"> the five Rs : <a href="/#main"> <i>main menu</i> </a> </h1>

        <br>

        <h2> "ratcheting" - doing purely positive things daily </h2>

        <br>

        <p> this ties into <a target="_blank" href="/five-fs">' the five Fs '</a> greatly </p>

        <br>

        <p> via striving to maintain and improve life ... </p>

        <br>

        <p> ... giving each of these major ways effort ... </p>

        <br>

        <p> ... we could , <a target="_blank" href="https://www.merriam-webster.com/dictionary/metaphorically">metaphorically</a> , <a target="_blank" href="https://share.google/cTtiinwMiekrT8JEM">ratchet</a> all of life </p>

        <br>

        <p> a ratchet doesn't allow reverse motions , or breaks </p>

        <br>

        <p> so , however greatly , minisculely , "ratcheting" assures progress ... </p>

        <br>

        <p> <a target="_blank" href="https://youtu.be/hmJyWreER7A?si=aNQQLSLU6uAxE28U"> ... consistently , positively , vulnerably : </a> </p>

        <br>

        <iframe width="560" height="315" src="https://www.youtube.com/embed/hmJyWreER7A?si=CuAGBdUnJRVK7tI8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>

        <br>

        <iframe width="560" height="315" src="https://www.youtube.com/embed/iCvmsMzlF7o?si=X7BKgTcpN15mWZVS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>

        <br>

        <p> further in this great theme and motif : </p>

        <br>

        <h3> <a href="https://zelda.fandom.com/wiki/Triforce">wisdom , courage , power</a> </h3>

        <br>

        <p> wisdom - knowing what to do , how , why </p>

        <br>

        <p> courage - responsiveness to Yeshu , Ga , love , wisdom </p>

        <br>

        <p> power - hammers wielded might build or hurt </p>

        <br>

        <br>

        <h3> strength , honor , valor </h3>

        <br>

        <p class="def"> strength - ability to exert forcefully , holistic potency </p>

        <br>

        <p class="def"> honor - more than only respect at distance , active </p>

        <br>

        <p class="def"> valor - openness to risking for others altruistically </p>

        <br>

        <br>

        <h2> replenishing </u>  Ga's* natural cycles ( flora , fauna , funga ) </h2>

        <br>

        <p> though it might seem strange , defecating , urinating  </p>

        <br>

        <p> upon soil to discerned need ( near vegetation ) </p>

        <br>

        <p> may help more than flushing it ( mayhaps ! ) </p>

        <br>

        <p> watering o'er-dry plants is obviously helpful </p>

        <br>

        <p> but all such behavior is needed often </p>

        <br>

        <br>

        <h2> reusing </u> rather than only and merely disposing </h2>

        <br>

        <p> insofar as reasonable , possible , " adds up " much ! </p>

        <br>

        <p> keeping metal , ceramic , wood , or plastic cups and plates </p>

        <br>

        <p> rather than repurchasing paper and Styrofoam ones </p>

        <br>

        <p> saves in many ways o'er lotsa time </p>

        <br>

        <p> lotsa - <a href="https://www.merriam-webster.com/dictionary/synonymous">synonymous</a> with beacoup in French , (very) much </p>

        <br>

        <br>

        <h2> refraining </u> from waste , negligence , harm , theft , murder </h2>

        <br>

        <p> such as avoiding purchasing slain animal flesh </p>

        <br>

        <p> oughta be " plain and simple " , obviously good </p>

        <br>

        <br>

        <h2> renewing  our minds , emboldening our good spirits </h2>

        <br>

        <p> becomes necessitated , required for our utmost achievements </p>

        <br>

        <p> hence such as music , dance , art and poetry </p>

        <br>

        <p> may be like unto " manna " for us </p>

        <br>

        <p> manna - the gifts of Heaven , Ga , Yeshu </p>

        <br>

        <br>

        <p> this may serve as exemplary such encouragement : </p>

        <br>

        <iframe style="display:block; margin:0 auto; border:none;" width="560" height="315" src="https://www.youtube.com/embed/GyOMYC6mlsY?si=tGeVCjRH_IL3XZNa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>

        <br>

        <iframe style="display:block; margin:0 auto; border:none;" width="560" height="315" src="https://www.youtube.com/embed/OiYjTb3opAA?si=8t9EvFTvZAhfPOPd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen> </iframe>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> wanna compassionately chat with ' <a href="/#mousey-pals">' Mousey-Pals '</a> ' & <a target="_blank" href="https://en.wikipedia.org/wiki/Captain_Planet_and_the_Planeteers">" Planeteers "</a> ? </p>

        <br>

        <p> we are about doing our duties joyously ! </p>

        <br>

        <p> such may join our Discord server : <a target="_blank" href="https://discord.gg/7GC366jj">Pals of Mousey-Qa</a> </p>

        <br>

        <br>

        <p> to ( kindly ) message this website's curator-creator ...</p>

        <br>

        <p> ... you may e-mail "Druce" : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <p> <i> novel notions <a target="_blank" href="collinsdictionary.com/dictionary/french-english/gratuit">gratuit</a> from Aware Advisory Services </i> </p>

        <br>

        <p> big thanks to the <a target="_blank" href="https://www.pythonanywhere.com/">PythonAnywhere.com</a> internet-service team </p>

        <br>

    </body>

    </html>

    """

@route('/ancient-truths')

def ancient_truu():

    return """

    <DOCTYPE! html>

    <head>

        <style>

            body {

                background-color: #000000;

                color: #FFFFFF;

                font-size: 2.62em;

                }



            p , ul , ol , h1 , h2 , h3 , h3 , h4 , h5 , h6   {

                color: #1aff1a;

                text-align: center;

                margin: 2px auto;

                }

            a {

                text-align: center;

                color: #00FFFF;

            }

            a.nn-page {

                color: yellow;

            }


            p.ylloh , h1.ylloh , h2.ylloh , h3.ylloh , h3.ylloh , h5.ylloh , h6.ylloh {

                color: yellow;

                margin: 2px auto;

                }

            p.def , p.ex {

                font-style: italic;

            }

            # p.ex for examples &/or explanations

            div.purple-line-thing {

                border-bottom: 3px dotted blue;

            }

            div.purple-line-thing {

                border-bottom: 3px dotted purple;

            }

            iframe {

                display:block;

                margin:0 auto;

                border:none;

            {

        </style>

    </head>

    <body>

        <h2> ancient truths </h2>

        <h3> <i> it is , we are , somehow like this ... </i> </h3>

        <h4> <a href="/#main">main links</a> <h4>

        <br>

        <ul>

            <li>

                <p> we could suffer and know joys ( both ) </p>

            </li>

                <br>

            <li>

                <p> causes of undesirable , desires , are knowable , discernible </p>

            </li>

                <br>

            <li>

                <p> each is avoidable , achievable ... might lessen , grow </p>

            </li>

                <br>

            <li>

                <p> for what's needed , " walking th' eightfold nobly " </p>

            </li>

                <br>

            <li>

                <p> how : resolve to live for everlasting goodness </p>

            </li>

        </ul>

        <br>

        <br>

        <p> " ... eightfold ?! " </p>

        <br>

        <p> yeah , quite so : </p>

        <br>

        <ul>

            <li>

                <p> veritable knowings - studious comprehension , factual knowledge , <a href="/ancient/#clair">clair-perceptivity</a> </p>

            </li>

                <br>

            <li>

                <p> dutiful awareness - remaining alert , sober enough , prayerful </p>

            </li>

                <br>

            <li>

                <p> apropos focus - concentration upon what's most needed </p>

            </li>

                <br>

            <li>

                <p> compassionate action - cautious , dynamically discerned ( gentle , unlazily ) </p>

            </li>

                <br>

            <li>

                <p> team-oriented talking - respectingly , honestly , proudly , humbly , kindly </p>

            </li>

                <br>

            <li>

                <p> buenos plans - Ga-given , critically thought , not not this </p>

            </li>

                <br>

            <li>

                <p> virtuous efforts - exerting " Goldilocks zone " , juhss so </p>

            </li>

                <br>

            <li>

                <p> befit livelihood - discovering and using our talents </p>

            </li>

            <br>

            <br>

            <p> lagniappe : laissez le bons temps roulez ! </p>

            <br>

            <p> ( French Creole ) </p>

            <br>

        </ul>

        <br>

        <h2 id="clair"> clair-perceptivity ( includes ) : </h2>

        <br>

            <ul>

                <li>

                    <p> clair-sentience - knowing(s) via experience(s) Yeshu gives </p>

                </li>

                    <br>

                <li>

                    <p> clair-cognizance - knowing(s) via serene thought(s) from Yeshu </p>

                </li>

                    <br>

                <li>

                    <p> clair-voyance - knowing(s) via appearance(s) from Yeshu </p>

                </li>

                    <br>

                <li>

                    <p> clair-audio - knowing(s) via sound(s) from Yeshu </p>

                </li>

                    <br>

                <li>

                    <p> clair-olfaction - knowing(s) via smell(s) from Yeshu </p>

                </li>

            </ul>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> wanna compassionately chat with ' <a href="/#mousey-pals">' Mousey-Pals '</a> ' & <a target="_blank" href="https://en.wikipedia.org/wiki/Captain_Planet_and_the_Planeteers">" Planeteers "</a> ? </p>

        <br>

        <p> we are about doing our duties joyously ! </p>

        <br>

        <p> such may join our Discord server : <a target="_blank" href="https://discord.gg/7GC366jj">Pals of Mousey-Qa</a> </p>

        <br>

        <br>

        <p> to ( kindly ) message this website's curator-creator ...</p>

        <br>

        <p> ... you may e-mail "Druce" : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <p> <i> novel notions <a target="_blank" href="collinsdictionary.com/dictionary/french-english/gratuit">gratuit</a> from Aware Advisory Services </i> </p>

        <br>

        <p> big thanks to the <a target="_blank" href="https://www.pythonanywhere.com/">PythonAnywhere.com</a> internet-service team </p>

        <br>

    </body>

    </html>


    """


@route('/duchee')

def duchee():

    return """

    <DOCTYPE! html>

    <head>

        <style>

            body {

                background-color: #000000;

                color: #FFFFFF;

                font-size: 2.62em;

                }



            p , ul , ol , h1 , h2 , h3 , h3 , h4 , h5 , h6   {

                color: #1aff1a;

                text-align: center;

                margin: 2px auto;

                }

            a {

                text-align: center;

                color: #00FFFF;

            }

            a.nn-page {

                color: yellow;

            }


            p.ylloh , h1.ylloh , h2.ylloh , h3.ylloh , h3.ylloh , h5.ylloh , h6.ylloh {

                color: yellow;

                margin: 2px auto;

                }

            p.def , p.ex {

                font-style: italic;

            }

            # p.ex for examples &/or explanations

            div.purple-line-thing {

                border-bottom: 3px dotted blue;

            }

            div.purple-line-thing {

                border-bottom: 3px dotted purple;

            }

            iframe {

                display:block;

                margin:0 auto;

                border:none;

            {

        </style>

    </head>

    <body>

        <h2> " duchee " </h2>

        <h3> <i> a how to ... </i> </h3>

        <br>

        <h4> <a href="/#main">return to main links</a> <h4>

        <br>
        <br>

        <p> duchee - associatively , <a href="https://www.merriam-webster.com/dictionary/categorically">categorially</a> , <a href="https://www.merriam-webster.com/dictionary/mathematically">mathematically</a> , <a href="https://www.merriam-webster.com/dictionary/organizational">organizationally</a> , pyudently satisying </p>

        <br>

        <p> associating - making some sorta correlation amongst thaengz </p>

        <br>

        <p> pyudently - <a href="https://www.merriam-webster.com/dictionary/productive">productive</a> , passionate , prurient , playful , yet <a href="/#pious">piously</a> </p>

        <br>

        <p> passionate - synonyms include " enthusiastic , ardent " ( <a href="https://www.merriam-webster.com/">Merriam-Webster</a> ) </p>

        <br>

        <p> prurient - purely positive consensuality : permission-based , prayerful </p>

        <br>
        <br>

        <p> an important " duchee " example is hand categorizing ... </p>

        <br>

        <p> these are " tried , true " general such associations : </p>

        <br>
        <br>

        <p> <u>thumb</u> : most general , commonly ordinary , surely helpful </p>

        <br>

        <p> <u>pointer</u> : genuine talent , authentic druther , personal expertise </p>

        <br>

        <p> <u>middle</u> : most needing <a href="https://www.merriam-webster.com/dictionary/moderation">moderation</a> ( of current " duchee " ) </p>

        <br>

        <p> <i> duchee is a ( quite ) versatile word , humbly </i> </p>

        <br>

        <p> <i> as noun : " a duchee " ; as verb : " duchee-ing " </p>

        <br>

        <p> <i> celebratorily ( for ' vehl* ' done associating ) : " duchee ! " </i> </p>

        <br>

        <p> <u>ring</u> : most related to matrimonial bliss , <a href="https://i1.sndcdn.com/artworks-LsSNxO14u9BRfjWn-SIs9tg-t500x500.jpg">friendship</a> </p>

        <br>

        <p> <u>pinky</u> : most related to <a href="https://www.youtube.com/c/PinkyPromise">friends keeping secrets</a> </p>

        <br>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> from <a href="/">feelings : emotions & sensations</a> : </p>

        <br>

        <p> glad | gladly :: joyous | happy | pleased | satisfied | contented </p>

        <br>

        <p> could you duchee with the above ? </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> here's our emotionality duchee : </p>

        <br>

        <p> joyous :: thumb </p>

        <br>

        <p> happy :: pointer </p>

        <br>

        <p> pleased :: middle </p>

        <br>

        <p> satisfied :: ring </p>

        <br>

        <p> contented :: pinky </p>

        <br>
        <br>

        <p> * vehl - replacing " well " for adverbial cases </p>

        <br>

        <p> well - a dug and built ( water ) well </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <h4> <a href="/#main">return to main links</a> <h4>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> wanna compassionately chat with ' <a href="/#mousey-pals">' Mousey-Pals '</a> ' & <a target="_blank" href="https://en.wikipedia.org/wiki/Captain_Planet_and_the_Planeteers">" Planeteers "</a> ? </p>

        <br>

        <p> we are about doing our duties joyously ! </p>

        <br>

        <p> such may join our Discord server : <a target="_blank" href="https://discord.gg/7GC366jj">Pals of Mousey-Qa</a> </p>

        <br>

        <br>

        <p> to ( kindly ) message this website's curator-creator ...</p>

        <br>

        <p> ... you may e-mail "Druce" : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <p> <i> novel notions <a target="_blank" href="collinsdictionary.com/dictionary/french-english/gratuit">gratuit</a> from Aware Advisory Services </i> </p>

        <br>

        <p> big thanks to the <a target="_blank" href="https://www.pythonanywhere.com/">PythonAnywhere.com</a> internet-service team </p>

        <br>

    </body>

    </html>


    """

@route('/definitions')

def defin():

    return """

    <DOCTYPE! html>

    <head>

        <style>

            body {

                background-color: #000000;

                color: #FFFFFF;

                font-size: 2.62em;

                }



            p , ul , ol , h1 , h2 , h3 , h3 , h4 , h5 , h6   {

                color: #1aff1a;

                text-align: center;

                margin: 2px auto;

                }

            a {

                text-align: center;

                color: #00FFFF;

            }

            a.nn-page {

                color: yellow;

            }


            p.ylloh , h1.ylloh , h2.ylloh , h3.ylloh , h3.ylloh , h5.ylloh , h6.ylloh {

                color: yellow;

                margin: 2px auto;

                }

            p.def , p.ex {

                font-style: italic;

            }

            # p.ex for examples &/or explanations

            div.purple-line-thing {

                border-bottom: 3px dotted blue;

            }

            div.purple-line-thing {

                border-bottom: 3px dotted purple;

            }

            iframe {

                display:block;

                margin:0 auto;

                border:none;

            {

        </style>

    </head>

    <body>

        <h2 id="defin"> new ( " Ilesk " ) word definitions list </h2>

        <br>

        <br>

        <p> duchee - associatively , <a href="https://www.merriam-webster.com/dictionary/categorically">categorially</a> , <a href="https://www.merriam-webster.com/dictionary/mathematically">mathematically</a> , <a href="https://www.merriam-webster.com/dictionary/organizational">organizationally</a> , pyudently satisying </p>

        <br>

        <p> * ee'n - replacing "even" insofar as " perhaps also " ... </p>

        <br>

        <p> ... but not for these numbers : 2 , 4 , <i> <a target="_blank" href="https://en.wikipedia.org/wiki/Et_cetera">etc.</a> </i> </p>

        <br>

        <p> pyudently - <a href="https://www.merriam-webster.com/dictionary/productive">productive</a> , passionate , prurient , playful , yet <a href="/#pious">piously</a> </p>

        <br>

        <p> * vehl - replacing " well " for adverbial cases ( " vehl done ! " ) </p>

        <br>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> wanna compassionately chat with ' <a href="/#mousey-pals">' Mousey-Pals '</a> ' & <a target="_blank" href="https://en.wikipedia.org/wiki/Captain_Planet_and_the_Planeteers">" Planeteers "</a> ? </p>

        <br>

        <p> we are about doing our duties joyously ! </p>

        <br>

        <p> such may join our Discord server : <a target="_blank" href="https://discord.gg/7GC366jj">Pals of Mousey-Qa</a> </p>

        <br>

        <br>

        <p> to ( kindly ) message this website's curator-creator ...</p>

        <br>

        <p> ... you may e-mail "Druce" : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <p> <i> novel notions <a target="_blank" href="collinsdictionary.com/dictionary/french-english/gratuit">gratuit</a> from Aware Advisory Services </i> </p>

        <br>

        <p> big thanks to the <a target="_blank" href="https://www.pythonanywhere.com/">PythonAnywhere.com</a> internet-service team </p>

        <br>

    </body>

    </html>

    """

@route('/Ilesk')

def Ilesk():

    return """

    <DOCTYPE! html>

    <head>

        <style>

            body {

                background-color: #000000;

                color: #FFFFFF;

                font-size: 2.62em;

                }



            p , ul , ol , h1 , h2 , h3 , h3 , h4 , h5 , h6   {

                color: #1aff1a;

                text-align: center;

                margin: 2px auto;

                }

            a {

                text-align: center;

                color: #00FFFF;

            }

            a.nn-page {

                color: yellow;

            }


            p.ylloh , h1.ylloh , h2.ylloh , h3.ylloh , h3.ylloh , h5.ylloh , h6.ylloh {

                color: yellow;

                margin: 2px auto;

                }

            p.def , p.ex {

                font-style: italic;

            }

            # p.ex for examples &/or explanations

            div.purple-line-thing {

                border-bottom: 3px dotted blue;

            }

            div.purple-line-thing {

                border-bottom: 3px dotted purple;

            }

            iframe {

                display:block;

                margin:0 auto;

                border:none;

            {

        </style>

    </head>

    <body>

        <h2 id="Ilesk"> " Ilesk " ihz a nuu laengw'j prajekt </h2>

        <br>

        <h2> <i> "Ilesk" is a new language project </i> </h2>

        <br>
        <br>

        <p> owr gohl 'z t hrrm'niiz ahl l'ngwihst'x ... </p>

        <br>

        <p> <i> our goal is to harmonize all linguistics ... </p>

        <br>

        <p> ... aand t so nnohvaet for ahptihm'l lihveeng </p>

        <br>

        <p> <i> ... and to so innovate for optimal living </i> </p>

        <br>

        <p> ihf nntreeg-d , qyureeuhss , maehaaps mes'j uhss ( b'loh ) ... </p>

        <br>

        <p> <i> if intrigued , curious , mayhaps message us ( below ) ... </i> </p>

        <br>

        <div class="purple-line-thing"> </div>

        <br>

        <p> wanna compassionately chat with <a href="/#mousey-pals">' Mousey-Pals '</a> & <a target="_blank" href="https://en.wikipedia.org/wiki/Captain_Planet_and_the_Planeteers">" Planeteers "</a> ? </p>

        <br>

        <p> we are about doing our duties joyously ! </p>

        <br>

        <p> such may join our Discord server : <a target="_blank" href="https://discord.gg/7GC366jj">Pals of Mousey-Qa</a> </p>

        <br>

        <br>

        <p> to ( kindly ) message this website's curator-creator ...</p>

        <br>

        <p> ... you may e-mail "Druce" : <a target="_blank" href="mailto:aindras.guillaume@proton.me">aindras.guillaume@proton.me</a> </p>

        <br>

        <p> <i> novel notions <a target="_blank" href="collinsdictionary.com/dictionary/french-english/gratuit">gratuit</a> from Aware Advisory Services </i> </p>

        <br>

        <p> big thanks to the <a target="_blank" href="https://www.pythonanywhere.com/">PythonAnywhere.com</a> internet-service team </p>

        <br>

    </body>

    </html>

    """

application = default_app()

#http://bit.ly/mousey-qa
