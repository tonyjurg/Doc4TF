<p>N1904 Greek New Testament Text-Fabric dataset (saulocantanhede/tfgreek2)</p>

<h1>Features per node type</h1>

<h2>book</h2>

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
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="book_short.md#readme">book_short</A></td>
  <td>string</td>
  <td>this is XML attribute book_short</td>
</tr>
<tr>
  <td><A HREF="lang.md#readme">lang</A></td>
  <td>string</td>
  <td>language the text is in</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
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
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>chapter number, from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>chapter number, from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td>integer</td>
  <td>verse number, from ref attribute in xml</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td>string</td>
  <td>clause type</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td>string</td>
  <td>clause type</td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td>string</td>
  <td>clause rule (from xml attribute Rule)</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td>integer</td>
  <td>node id (as in the XML source data</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td>string</td>
  <td>this is XML attribute typ</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td>string</td>
  <td>clause type</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td>string</td>
  <td>clause type</td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td>string</td>
  <td>clause rule (from xml attribute Rule)</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td>integer</td>
  <td>node id (as in the XML source data</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="appositioncontainer.md#readme">appositioncontainer</A></td>
  <td>integer</td>
  <td>1 if it is an apposition container</td>
</tr>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="clauseType.md#readme">clauseType</A></td>
  <td>string</td>
  <td>clause type</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
</tr>
<tr>
  <td><A HREF="cltype.md#readme">cltype</A></td>
  <td>string</td>
  <td>clause type</td>
</tr>
<tr>
  <td><A HREF="crule.md#readme">crule</A></td>
  <td>string</td>
  <td>clause rule (from xml attribute Rule)</td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td>string</td>
  <td>this is XML attribute function</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
</tr>
<tr>
  <td><A HREF="nodeId.md#readme">nodeId</A></td>
  <td>integer</td>
  <td>node id (as in the XML source data</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td>string</td>
  <td>this is XML attribute rela</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td>string</td>
  <td>this is XML attribute typ</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>material after the end of the word</td>
</tr>
<tr>
  <td><A HREF="appositioncontainer.md#readme">appositioncontainer</A></td>
  <td>integer</td>
  <td>1 if it is an apposition container</td>
</tr>
<tr>
  <td><A HREF="articular.md#readme">articular</A></td>
  <td>integer</td>
  <td>1 if the wg has an article</td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td>string</td>
  <td>this is XML attribute before</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>grammatical case</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td>string</td>
  <td>this is XML attribute criticalsign</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>grammatical degree</td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td>integer</td>
  <td>1 if the word is out of sequence in the xml</td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td>string</td>
  <td>domain</td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td>string</td>
  <td>this is XML attribute framespec</td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td>string</td>
  <td>this is XML attribute function</td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td>string</td>
  <td>grammatical gender</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>short translation</td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td>string</td>
  <td>xml id</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td>string</td>
  <td>type of junction</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>lexical lemma</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>ln</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>verbal mood</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>morphological code</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>lemma normalized</td>
</tr>
<tr>
  <td><A HREF="note.md#readme">note</A></td>
  <td>string</td>
  <td>annotation of linguistic nature</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>grammatical number</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>grammatical person</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>this is XML attribute punctuation</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>biblical reference with word counting</td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td>string</td>
  <td>number of referent</td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td>string</td>
  <td>this is XML attribute rela</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
</tr>
<tr>
  <td><A HREF="rule.md#readme">rule</A></td>
  <td>string</td>
  <td>syntactical rule</td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td>integer</td>
  <td>strong number</td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td>string</td>
  <td>this is XML attribute subjrefspec</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>verbal tense</td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td>string</td>
  <td>the text of a word</td>
</tr>
<tr>
  <td><A HREF="typ.md#readme">typ</A></td>
  <td>string</td>
  <td>this is XML attribute typ</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>word in unicode characters plus material after it</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>verbal voice</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>material after the end of the word</td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td>string</td>
  <td>this is XML attribute before</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>grammatical case</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td>string</td>
  <td>this is XML attribute criticalsign</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>grammatical degree</td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td>integer</td>
  <td>1 if the word is out of sequence in the xml</td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td>string</td>
  <td>domain</td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td>string</td>
  <td>this is XML attribute framespec</td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td>string</td>
  <td>grammatical gender</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>short translation</td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td>string</td>
  <td>xml id</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>lexical lemma</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>ln</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>verbal mood</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>morphological code</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>lemma normalized</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>grammatical number</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>grammatical person</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>this is XML attribute punctuation</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>biblical reference with word counting</td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td>string</td>
  <td>number of referent</td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td>integer</td>
  <td>strong number</td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td>string</td>
  <td>this is XML attribute subjrefspec</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>verbal tense</td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td>string</td>
  <td>the text of a word</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>word in unicode characters plus material after it</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>verbal voice</td>
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
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td>string</td>
  <td>material after the end of the word</td>
</tr>
<tr>
  <td><A HREF="before.md#readme">before</A></td>
  <td>string</td>
  <td>this is XML attribute before</td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td>string</td>
  <td>book name (abbreviated), from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="book_short.md#readme">book_short</A></td>
  <td>string</td>
  <td>this is XML attribute book_short</td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td>string</td>
  <td>grammatical case</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td>integer</td>
  <td>chapter number, from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="cls.md#readme">cls</A></td>
  <td>string</td>
  <td>this is XML attribute cls</td>
</tr>
<tr>
  <td><A HREF="criticalsign.md#readme">criticalsign</A></td>
  <td>string</td>
  <td>this is XML attribute criticalsign</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td>string</td>
  <td>grammatical degree</td>
</tr>
<tr>
  <td><A HREF="discontinuous.md#readme">discontinuous</A></td>
  <td>integer</td>
  <td>1 if the word is out of sequence in the xml</td>
</tr>
<tr>
  <td><A HREF="domain.md#readme">domain</A></td>
  <td>string</td>
  <td>domain</td>
</tr>
<tr>
  <td><A HREF="framespec.md#readme">framespec</A></td>
  <td>string</td>
  <td>this is XML attribute framespec</td>
</tr>
<tr>
  <td><A HREF="function.md#readme">function</A></td>
  <td>string</td>
  <td>this is XML attribute function</td>
</tr>
<tr>
  <td><A HREF="gender.md#readme">gender</A></td>
  <td>string</td>
  <td>grammatical gender</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td>string</td>
  <td>short translation</td>
</tr>
<tr>
  <td><A HREF="id.md#readme">id</A></td>
  <td>string</td>
  <td>xml id</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td>string</td>
  <td>lexical lemma</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td>string</td>
  <td>ln</td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td>string</td>
  <td>verbal mood</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td>string</td>
  <td>morphological code</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td>string</td>
  <td>lemma normalized</td>
</tr>
<tr>
  <td><A HREF="note.md#readme">note</A></td>
  <td>string</td>
  <td>annotation of linguistic nature</td>
</tr>
<tr>
  <td><A HREF="num.md#readme">num</A></td>
  <td>integer</td>
  <td>generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td>string</td>
  <td>grammatical number</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td>string</td>
  <td>No feature description</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td>string</td>
  <td>grammatical person</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td>string</td>
  <td>this is XML attribute punctuation</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td>string</td>
  <td>biblical reference with word counting</td>
</tr>
<tr>
  <td><A HREF="referent.md#readme">referent</A></td>
  <td>string</td>
  <td>number of referent</td>
</tr>
<tr>
  <td><A HREF="rela.md#readme">rela</A></td>
  <td>string</td>
  <td>this is XML attribute rela</td>
</tr>
<tr>
  <td><A HREF="role.md#readme">role</A></td>
  <td>string</td>
  <td>role</td>
</tr>
<tr>
  <td><A HREF="strong.md#readme">strong</A></td>
  <td>integer</td>
  <td>strong number</td>
</tr>
<tr>
  <td><A HREF="subjrefspec.md#readme">subjrefspec</A></td>
  <td>string</td>
  <td>this is XML attribute subjrefspec</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td>string</td>
  <td>verbal tense</td>
</tr>
<tr>
  <td><A HREF="text.md#readme">text</A></td>
  <td>string</td>
  <td>the text of a word</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td>string</td>
  <td>morphological type (on w), syntactical type (on wg)</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td>string</td>
  <td>word in unicode characters plus material after it</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td>integer</td>
  <td>verse number, from ref attribute in xml</td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td>string</td>
  <td>verbal voice</td>
</tr>
</tbody>
</table>
