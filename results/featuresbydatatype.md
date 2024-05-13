N1904 Greek New Testament <a href="https://github.com/saulocantanhede/tfgreek2">saulocantanhede/tfgreek2 - 0.5.7</a>
# Overview features per datatype
## Integer

Feature|Featuretype|Available on nodes|Description|Examples
---|---|---|---|---
[`appositioncontainer`](appositioncontainer.md#readme)|[`Node`](featuresbytype.md#node)|[`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) |1 if it is an apposition container|`1`
[`articular`](articular.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) |1 if the sentence, group, clause, phrase or wg has an article|`1`
[`chapter`](chapter.md#readme)|[`Node`](featuresbytype.md#node)|[`chapter`](featuresbynodetype.md#chapter) [`verse`](featuresbynodetype.md#verse) [`word`](featuresbynodetype.md#word) |chapter number, from ref attribute in xml|`1` `2` `3` `4`
[`discontinuous`](discontinuous.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |1 if the word is out of sequence in the xml|`1`
[`nodeid`](nodeid.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) |node id (as in the XML source data|`400040070010120` `400040100010070` `400050030010120` `400050040010060`
[`num`](num.md#readme)|[`Node`](featuresbytype.md#node)|[`book`](featuresbynodetype.md#book) [`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.|`1` `2` `3` `4`
[`strong`](strong.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |strong number|`846` `3004` `1510` `4771`
[`verse`](verse.md#readme)|[`Node`](featuresbytype.md#node)|[`verse`](featuresbynodetype.md#verse) [`word`](featuresbynodetype.md#word) |verse number, from ref attribute in xml|`1` `2` `3` `4`
[`sibling`](sibling.md#readme)|[`Edge`](featuresbytype.md#edge)|[`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute sibling|`1` `2` `3` `4`
## String

Feature|Featuretype|Available on nodes|Description|Examples
---|---|---|---|---
[`after`](after.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |material after the end of the word|` ` `,` `.` `·`
[`before`](before.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute before|`—` `(` `[[`
[`book`](book.md#readme)|[`Node`](featuresbytype.md#node)|[`book`](featuresbynodetype.md#book) [`chapter`](featuresbynodetype.md#chapter) [`verse`](featuresbynodetype.md#verse) [`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`word`](featuresbynodetype.md#word) |book name (full name)|`Acts` `Colossians` `Ephesians` `Galatians`
[`bookshort`](bookshort.md#readme)|[`Node`](featuresbytype.md#node)|[`book`](featuresbynodetype.md#book) [`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`word`](featuresbynodetype.md#word) |book name (abbreviated) from ref attribute in xml|`1CO` `1JN` `1PE` `1TH`
[`case`](case.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |grammatical case|`nominative` `accusative` `dative` `genitive`
[`clausetype`](clausetype.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) |clause type|`nominalized`
[`cls`](cls.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute cls|`cl`
[`cltype`](cltype.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) |clause type|`Verbless` `VerbElided` `Minor`
[`criticalsign`](criticalsign.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute criticalsign|`—` `)` `(` `]]`
[`crule`](crule.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) |clause rule (from xml attribute Rule)|`ClCl` `ClCl2`
[`degree`](degree.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |grammatical degree|`comparative` `superlative`
[`domain`](domain.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |domain|`092004` `033006` `013001` `069002`
[`framespec`](framespec.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute framespec|`A0:n00000000000` `A1:n00000000000` `A0:n47010001004` `A0:n46003022002`
[`function`](function.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute function|`Pred-Obj` `Subj-PreC-PreC` `Cmpl-Pred` `Cmpl-Pred-Obj`
[`gender`](gender.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |grammatical gender|`masculine` `neuter` `feminine`
[`gloss`](gloss.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |short translation|`not` `you` `is` `Him`
[`id`](id.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |xml id|`n40001002001` `n40001002002` `n40001002005` `n40001002007`
[`junction`](junction.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) |type of junction|`coordinate` `subordinate`
[`lang`](lang.md#readme)|[`Node`](featuresbytype.md#node)|[`book`](featuresbynodetype.md#book) |language the text is in|`el`
[`lemma`](lemma.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |lexical lemma|`αὐτός` `λέγω` `εἰμί` `σύ`
[`lemmatranslit`](lemmatranslit.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |transliteration of the word lemma|`autos` `lego` `eimi` `su`
[`ln`](ln.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |ln|`92.11` `33.69` `69.3` `92.1`
[`mood`](mood.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |verbal mood|`indicative` `participle` `infinitive` `subjunctive`
[`morph`](morph.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |morphological code|`V-PAI-3S` `ADV` `PRT-N` `V-2AAI-3S`
[`normalized`](normalized.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |lemma normalized|`αὐτόν` `μή` `αὐτῷ` `οὐκ`
[`note`](note.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |annotation of linguistic nature|`discontinuous discourse`
[`number`](number.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |grammatical number|`singular` `plural`
[`otype`](otype.md#readme)|[`Node`](featuresbytype.md#node)||No feature description|No values
[`person`](person.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |grammatical person|`third` `second` `first`
[`punctuation`](punctuation.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute punctuation|` ` `,` `.` `·`
[`ref`](ref.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |biblical reference with word counting|`1CO 10:1!1` `1CO 10:1!15` `1CO 10:1!17` `1CO 10:1!2`
[`referent`](referent.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |number of referent|`n40005001015` `n43014023002` `n43013023006 n43013037003 n43014005003 n43014008003 n43014022003` `n43017001003`
[`rela`](rela.md#readme)|[`Node`](featuresbytype.md#node)|[`wg`](featuresbynodetype.md#wg) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute rela|`Appo`
[`role`](role.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |role|`adv` `o` `s` `apposition`
[`rule`](rule.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) |syntactical rule|`Conj-CL` `CLaCL` `sub-CL` `DetCL`
[`sp`](sp.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |part-of-speach|`verb` `pron` `advb` `subs`
[`subjrefspec`](subjrefspec.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute subjrefspec|`n46003022002` `n66001009002` `n45001001001` `n47010001004`
[`tense`](tense.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |verbal tense|`aorist` `present` `future` `imperfect`
[`text`](text.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |the text of a word|`αὐτῷ` `μὴ` `οὐκ` `εἶπεν`
[`trans`](trans.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |translation of the word surface text according to the Berean Interlinear Bible|`not` `you` `is` `Him`
[`translit`](translit.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |transliteration of the word surface text|`me` `estin` `auton` `auto`
[`typ`](typ.md#readme)|[`Node`](featuresbytype.md#node)|[`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) |this is XML attribute typ|`conjuncted` `apposition`
[`type`](type.md#readme)|[`Node`](featuresbytype.md#node)|[`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)|`wrapper-clause-scope` `group` `apposition-group`
[`unaccent`](unaccent.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |word in unicode characters without accents and diacritical markers|`εστιν` `αυτον` `μη` `αυτω`
[`unicode`](unicode.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |word in unicode characters plus material after it|`μὴ` `οὐκ` `αὐτῷ` `εἶπεν`
[`variant`](variant.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |this is XML attribute variant|`2` `1`
[`voice`](voice.md#readme)|[`Node`](featuresbytype.md#node)|[`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |verbal voice|`active` `passive` `middle` `middlepassive`
[`frame`](frame.md#readme)|[`Edge`](featuresbytype.md#edge)|[`word`](featuresbynodetype.md#word) |frame|`A0` `A1` `A2` `AA2`
[`oslots`](oslots.md#readme)|[`Edge`](featuresbytype.md#edge)||No feature description|No values
[`parent`](parent.md#readme)|[`Edge`](featuresbytype.md#edge)|[`sentence`](featuresbynodetype.md#sentence) [`group`](featuresbynodetype.md#group) [`clause`](featuresbynodetype.md#clause) [`wg`](featuresbynodetype.md#wg) [`phrase`](featuresbynodetype.md#phrase) [`subphrase`](featuresbynodetype.md#subphrase) [`word`](featuresbynodetype.md#word) |parent relationship between words|`Link`
[`subjref`](subjref.md#readme)|[`Edge`](featuresbytype.md#edge)|[`word`](featuresbynodetype.md#word) |number of subject referent|`Link`


Created on May. 13, 2024 using [Doc4TF version 0.5 (May. 13, 2024)](https://github.com/tonyjurg/Doc4TF/blob/main/CreateFeatureDoc.ipynb)