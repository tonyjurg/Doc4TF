<p>N1904 Greek New Testament Text-Fabric dataset (saulocantanhede/tfgreek2)</p>

<h1>Features per node type</h1>

<h2>book</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="book_short.md#readme">book_short</A></td>
  <td>string</td>
  <td>this is XML attribute book_short</td>
  <td>LUK ACT</td>
</tr>
<tr>
  <td><A HREF="lang.md#readme">lang</A></td>
  <td>string</td>
  <td>language the text is in</td>
  <td>el</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
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
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>chapter number, from ref attribute in xml</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
</tbody>
</table>

<h2>verse</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>chapter number, from ref attribute in xml</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td>integer</td>
  <td>verse number, from ref attribute in xml</td>
  <td>10 12</td>
</tr>
</tbody>
</table>

<h2>sentence</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td>string</td>
  <td>clause type</td>
  <td>nominalized</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
  <td>np cl</td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td>string</td>
  <td>clause type</td>
  <td>VerbElided Verbless</td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td>string</td>
  <td>clause rule (from xml attribute Rule)</td>
  <td>ClCl ClCl2</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
  <td>coordinate subordinate</td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td>integer</td>
  <td>node id (as in the XML source data</td>
  <td>400010200010490 400010200120390</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
  <td>v adv</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
  <td>DetNP PrepNp</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
</tbody>
</table>

<h2>group</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
  <td>v adv</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
  <td>DetNP PrepNp</td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td>string</td>
  <td>this is XML attribute typ</td>
  <td>NP PP</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
</tbody>
</table>

<h2>clause</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td>string</td>
  <td>clause type</td>
  <td>nominalized</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
  <td>np cl</td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td>string</td>
  <td>clause type</td>
  <td>VerbElided Verbless</td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td>string</td>
  <td>clause rule (from xml attribute Rule)</td>
  <td>ClCl ClCl2</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
  <td>coordinate subordinate</td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td>integer</td>
  <td>node id (as in the XML source data</td>
  <td>400010200010490 400010200120390</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
  <td>v adv</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
  <td>DetNP PrepNp</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
</tbody>
</table>

<h2>wg</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="appositioncontainer.md#readme">appositioncontainer</A></td>
  <td>integer</td>
  <td>1 if it is an apposition container</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td>string</td>
  <td>clause type</td>
  <td>nominalized</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
  <td>np cl</td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td>string</td>
  <td>clause type</td>
  <td>VerbElided Verbless</td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td>string</td>
  <td>clause rule (from xml attribute Rule)</td>
  <td>ClCl ClCl2</td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td>string</td>
  <td>this is XML attribute function</td>
  <td>Pred Subj</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
  <td>coordinate subordinate</td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td>integer</td>
  <td>node id (as in the XML source data</td>
  <td>400010200010490 400010200120390</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td>string</td>
  <td>this is XML attribute rela</td>
  <td>Appo</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
  <td>v adv</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
  <td>DetNP PrepNp</td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td>string</td>
  <td>this is XML attribute typ</td>
  <td>NP PP</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
</tbody>
</table>

<h2>phrase</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>material after the end of the word</td>
  <td>, .</td>
</tr>
<tr>
  <td><A HREF="appositioncontainer.md#readme">appositioncontainer</A></td>
  <td>integer</td>
  <td>1 if it is an apposition container</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td>string</td>
  <td>this is XML attribute before</td>
  <td>— (</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>grammatical case</td>
  <td>nominative accusative</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
  <td>np cl</td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td>string</td>
  <td>this is XML attribute criticalsign</td>
  <td>— (</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>grammatical degree</td>
  <td>comparative superlative</td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td>integer</td>
  <td>1 if the word is out of sequence in the xml</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td>string</td>
  <td>domain</td>
  <td>092004 089017</td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td>string</td>
  <td>this is XML attribute framespec</td>
  <td>A0:n00000000000 A1:n00000000000</td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td>string</td>
  <td>this is XML attribute function</td>
  <td>Pred Subj</td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td>string</td>
  <td>grammatical gender</td>
  <td>masculine feminine</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>short translation</td>
  <td>the and</td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td>string</td>
  <td>xml id</td>
  <td>n40001001001 n40001001002</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
  <td>coordinate subordinate</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>lexical lemma</td>
  <td>ὁ καί</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>ln</td>
  <td>92.24 92.11</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>verbal mood</td>
  <td>indicative participle</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>morphological code</td>
  <td>CONJ PREP</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>lemma normalized</td>
  <td>καί ὁ</td>
</tr>
<tr>
  <td><A HREF="note.md#readme">note</A></td>
  <td>string</td>
  <td>annotation of linguistic nature</td>
  <td>discontinuous discourse</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>grammatical number</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>grammatical person</td>
  <td>third second</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>this is XML attribute punctuation</td>
  <td>, .</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>biblical reference with word counting</td>
  <td>1CO 10:1!1 1CO 10:1!10</td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td>string</td>
  <td>number of referent</td>
  <td>n40005001015 n43014023002</td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td>string</td>
  <td>this is XML attribute rela</td>
  <td>Appo</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
  <td>v adv</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
  <td>DetNP PrepNp</td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td>integer</td>
  <td>strong number</td>
  <td>3588 2532</td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td>string</td>
  <td>this is XML attribute subjrefspec</td>
  <td>n46003022002 n66001009002</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>verbal tense</td>
  <td>aorist present</td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td>string</td>
  <td>the text of a word</td>
  <td>καὶ ὁ</td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td>string</td>
  <td>this is XML attribute typ</td>
  <td>NP PP</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>word in unicode characters plus material after it</td>
  <td>καὶ ὁ</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>verbal voice</td>
  <td>active passive</td>
</tr>
</tbody>
</table>

<h2>subphrase</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>material after the end of the word</td>
  <td>, .</td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td>string</td>
  <td>this is XML attribute before</td>
  <td>— (</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>grammatical case</td>
  <td>nominative accusative</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
  <td>np cl</td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td>string</td>
  <td>this is XML attribute criticalsign</td>
  <td>— (</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>grammatical degree</td>
  <td>comparative superlative</td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td>integer</td>
  <td>1 if the word is out of sequence in the xml</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td>string</td>
  <td>domain</td>
  <td>092004 089017</td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td>string</td>
  <td>this is XML attribute framespec</td>
  <td>A0:n00000000000 A1:n00000000000</td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td>string</td>
  <td>grammatical gender</td>
  <td>masculine feminine</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>short translation</td>
  <td>the and</td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td>string</td>
  <td>xml id</td>
  <td>n40001001001 n40001001002</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>lexical lemma</td>
  <td>ὁ καί</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>ln</td>
  <td>92.24 92.11</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>verbal mood</td>
  <td>indicative participle</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>morphological code</td>
  <td>CONJ PREP</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>lemma normalized</td>
  <td>καί ὁ</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>grammatical number</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>grammatical person</td>
  <td>third second</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>this is XML attribute punctuation</td>
  <td>, .</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>biblical reference with word counting</td>
  <td>1CO 10:1!1 1CO 10:1!10</td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td>string</td>
  <td>number of referent</td>
  <td>n40005001015 n43014023002</td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td>integer</td>
  <td>strong number</td>
  <td>3588 2532</td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td>string</td>
  <td>this is XML attribute subjrefspec</td>
  <td>n46003022002 n66001009002</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>verbal tense</td>
  <td>aorist present</td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td>string</td>
  <td>the text of a word</td>
  <td>καὶ ὁ</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>word in unicode characters plus material after it</td>
  <td>καὶ ὁ</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>verbal voice</td>
  <td>active passive</td>
</tr>
</tbody>
</table>

<h2>word</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>material after the end of the word</td>
  <td>, .</td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td>string</td>
  <td>this is XML attribute before</td>
  <td>— (</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
  <td>Luke Matthew</td>
</tr>
<tr>
  <td><A HREF="book_short.md#readme">book_short</A></td>
  <td>string</td>
  <td>this is XML attribute book_short</td>
  <td>LUK ACT</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>grammatical case</td>
  <td>nominative accusative</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>chapter number, from ref attribute in xml</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
  <td>np cl</td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td>string</td>
  <td>this is XML attribute criticalsign</td>
  <td>— (</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>grammatical degree</td>
  <td>comparative superlative</td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td>integer</td>
  <td>1 if the word is out of sequence in the xml</td>
  <td>1</td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td>string</td>
  <td>domain</td>
  <td>092004 089017</td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td>string</td>
  <td>this is XML attribute framespec</td>
  <td>A0:n00000000000 A1:n00000000000</td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td>string</td>
  <td>this is XML attribute function</td>
  <td>Pred Subj</td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td>string</td>
  <td>grammatical gender</td>
  <td>masculine feminine</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>short translation</td>
  <td>the and</td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td>string</td>
  <td>xml id</td>
  <td>n40001001001 n40001001002</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>lexical lemma</td>
  <td>ὁ καί</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>ln</td>
  <td>92.24 92.11</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>verbal mood</td>
  <td>indicative participle</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>morphological code</td>
  <td>CONJ PREP</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>lemma normalized</td>
  <td>καί ὁ</td>
</tr>
<tr>
  <td><A HREF="note.md#readme">note</A></td>
  <td>string</td>
  <td>annotation of linguistic nature</td>
  <td>discontinuous discourse</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
  <td>1 2</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>grammatical number</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
  <td>singular plural</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>grammatical person</td>
  <td>third second</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>this is XML attribute punctuation</td>
  <td>, .</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>biblical reference with word counting</td>
  <td>1CO 10:1!1 1CO 10:1!10</td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td>string</td>
  <td>number of referent</td>
  <td>n40005001015 n43014023002</td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td>string</td>
  <td>this is XML attribute rela</td>
  <td>Appo</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
  <td>v adv</td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td>integer</td>
  <td>strong number</td>
  <td>3588 2532</td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td>string</td>
  <td>this is XML attribute subjrefspec</td>
  <td>n46003022002 n66001009002</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>verbal tense</td>
  <td>aorist present</td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td>string</td>
  <td>the text of a word</td>
  <td>καὶ ὁ</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
  <td>modifier-scope common</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>word in unicode characters plus material after it</td>
  <td>καὶ ὁ</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td>integer</td>
  <td>verse number, from ref attribute in xml</td>
  <td>10 12</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>verbal voice</td>
  <td>active passive</td>
</tr>
</tbody>
</table>
