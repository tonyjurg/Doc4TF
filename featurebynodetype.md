<h1>Features per node type</h1>

<h2>Nodetype: book</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>✅ Book name (in English language)</td>
</tr>
<tr>
  <td><A HREF="booknumber.md#readme">booknumber</A></td>
  <td>integer</td>
  <td>✅ NT book number (Matthew=1, Mark=2, ..., Revelation=27)</td>
</tr>
<tr>
  <td><A HREF="bookshort.md#readme">bookshort</A></td>
  <td>string</td>
  <td>✅ Book name (abbreviated)</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
</tbody>
</table>

<h2>chapter</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>✅ Book name (in English language)</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>✅ Chapter number inside book</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
</tbody>
</table>

<h2>Nodetype: verse</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>✅ Book name (in English language)</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>✅ Chapter number inside book</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td>integer</td>
  <td>✅ Verse number inside chapter</td>
</tr>
</tbody>
</table>

<h2>Nodetype: sentence</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>✅ Book name (in English language)</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>✅ Chapter number inside book</td>
</tr>
<tr>
  <td><A HREF="headverse.md#readme">headverse</A></td>
  <td>string</td>
  <td>✅ Start verse number of a sentence</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="sentence.md#readme">sentence</A></td>
  <td>integer</td>
  <td>✅ Sentence number (counted per chapter)</td>
</tr>
</tbody>
</table>

<h2>Nodetype: wg</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="clausetype.md#readme">clausetype</A></td>
  <td>string</td>
  <td>✅ Clause type details (e.g. Verbless, Minor)</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>✅ Junction data related to a wordgroup</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="wgclass.md#readme">wgclass</A></td>
  <td>string</td>
  <td>✅ Class of the wordgroup (e.g. cl, np, vp)</td>
</tr>
<tr>
  <td><A HREF="wglevel.md#readme">wglevel</A></td>
  <td>integer</td>
  <td>🆗 Number of the parent wordgroups for a wordgroup</td>
</tr>
<tr>
  <td><A HREF="wgnum.md#readme">wgnum</A></td>
  <td>integer</td>
  <td>✅ Wordgroup number (counted per book)</td>
</tr>
<tr>
  <td><A HREF="wgrole.md#readme">wgrole</A></td>
  <td>string</td>
  <td>✅ Syntactical role of the wordgroup (abbreviated)</td>
</tr>
<tr>
  <td><A HREF="wgrolelong.md#readme">wgrolelong</A></td>
  <td>string</td>
  <td>✅ Syntactical role of the wordgroup (full)</td>
</tr>
<tr>
  <td><A HREF="wgrule.md#readme">wgrule</A></td>
  <td>string</td>
  <td>✅ Wordgroup rule information (e.g. Np-Appos, ClCl2, PrepNp)</td>
</tr>
<tr>
  <td><A HREF="wgtype.md#readme">wgtype</A></td>
  <td>string</td>
  <td>✅ Wordgroup type details (e.g. group, apposition)</td>
</tr>
</tbody>
</table>

<h2>Nodetype: word</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>✅ Characters (eg. punctuations) following the word</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>✅ Book name (in English language)</td>
</tr>
<tr>
  <td><A HREF="booknumber.md#readme">booknumber</A></td>
  <td>integer</td>
  <td>✅ NT book number (Matthew=1, Mark=2, ..., Revelation=27)</td>
</tr>
<tr>
  <td><A HREF="bookshort.md#readme">bookshort</A></td>
  <td>string</td>
  <td>✅ Book name (abbreviated)</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>✅ Gramatical case (Nominative, Genitive, Dative, Accusative, Vocative)</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>✅ Chapter number inside book</td>
</tr>
<tr>
  <td><A HREF="containedclause.md#readme">containedclause</A></td>
  <td>string</td>
  <td>🆗 Contained clause (WG number)</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>✅ Degree (e.g. Comparitative, Superlative)</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>✅ English gloss</td>
</tr>
<tr>
  <td><A HREF="gn.md#readme">gn</A></td>
  <td>string</td>
  <td>✅ Gramatical gender (Masculine, Feminine, Neuter)</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>✅ Lexeme (lemma)</td>
</tr>
<tr>
  <td><A HREF="lex_dom.md#readme">lex_dom</A></td>
  <td>string</td>
  <td>✅ Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG (not present everywhere?)</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>✅ Lauw-Nida lexical classification (not present everywhere?)</td>
</tr>
<tr>
  <td><A HREF="markafter.md#readme">markafter</A></td>
  <td>string</td>
  <td>🆗 Text critical marker after word</td>
</tr>
<tr>
  <td><A HREF="markbefore.md#readme">markbefore</A></td>
  <td>string</td>
  <td>🆗 Text critical marker before word</td>
</tr>
<tr>
  <td><A HREF="markorder.md#readme">markorder</A></td>
  <td>string</td>
  <td>Order of punctuation and text critical marker</td>
</tr>
<tr>
  <td><A HREF="monad.md#readme">monad</A></td>
  <td>integer</td>
  <td>✅ Monad (smallest token matching word order in the corpus)</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>✅ Gramatical mood of the verb (passive, etc)</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>✅ Morphological tag (Sandborg-Petersen morphology)</td>
</tr>
<tr>
  <td><A HREF="nodeID.md#readme">nodeID</A></td>
  <td>string</td>
  <td>✅ Node ID (as in the XML source data)</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>✅ Surface word with accents normalized and trailing punctuations removed</td>
</tr>
<tr>
  <td><A HREF="nu.md#readme">nu</A></td>
  <td>string</td>
  <td>✅ Gramatical number (Singular, Plural)</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>✅ Gramatical number of the verb (e.g. singular, plural)</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>✅ Gramatical person of the verb (first, second, third)</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>✅ Punctuation after word</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>✅ Value of the ref ID (taken from XML sourcedata)</td>
</tr>
<tr>
  <td><A HREF="reference.md#readme">reference</A></td>
  <td>string</td>
  <td>✅ Reference (to nodeID in XML source data, not yet post-processes)</td>
</tr>
<tr>
  <td><A HREF="roleclausedistance.md#readme">roleclausedistance</A></td>
  <td>string</td>
  <td>⚠️ Distance to the wordgroup defining the syntactical role of this word</td>
</tr>
<tr>
  <td><A HREF="sentence.md#readme">sentence</A></td>
  <td>integer</td>
  <td>✅ Sentence number (counted per chapter)</td>
</tr>
<tr>
  <td><A HREF="sp.md#readme">sp</A></td>
  <td>string</td>
  <td>✅ Part of Speech (abbreviated)</td>
</tr>
<tr>
  <td><A HREF="sp_full.md#readme">sp_full</A></td>
  <td>string</td>
  <td>✅ Part of Speech (long description)</td>
</tr>
<tr>
  <td><A HREF="strongs.md#readme">strongs</A></td>
  <td>string</td>
  <td>✅ Strongs number</td>
</tr>
<tr>
  <td><A HREF="subj_ref.md#readme">subj_ref</A></td>
  <td>string</td>
  <td>🆗 Subject reference (to nodeID in XML source data, not yet post-processes)</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>✅ Gramatical tense of the verb (e.g. Present, Aorist)</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>✅ Gramatical type  of noun or pronoun (e.g. Common, Personal)</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>✅ Word as it apears in the text in Unicode (incl. punctuations)</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td>integer</td>
  <td>✅ Verse number inside chapter</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>✅ Gramatical voice of the verb (e.g. active,passive)</td>
</tr>
<tr>
  <td><A HREF="word.md#readme">word</A></td>
  <td>string</td>
  <td>✅ Word as it appears in the text (excl. punctuations)</td>
</tr>
<tr>
  <td><A HREF="wordlevel.md#readme">wordlevel</A></td>
  <td>string</td>
  <td>🆗 Number of the parent wordgroups for a word</td>
</tr>
<tr>
  <td><A HREF="wordrole.md#readme">wordrole</A></td>
  <td>string</td>
  <td>✅ Syntactical role of the word (abbreviated)</td>
</tr>
<tr>
  <td><A HREF="wordrolelong.md#readme">wordrolelong</A></td>
  <td>string</td>
  <td>✅ Syntactical role of the word (full)</td>
</tr>
<tr>
  <td><A HREF="wordtranslit.md#readme">wordtranslit</A></td>
  <td>string</td>
  <td>🆗 Transliteration of the text (in latin letters, excl. punctuations)</td>
</tr>
<tr>
  <td><A HREF="wordunacc.md#readme">wordunacc</A></td>
  <td>string</td>
  <td>✅ Word without accents (excl. punctuations)</td>
</tr>
</tbody>
</table>
