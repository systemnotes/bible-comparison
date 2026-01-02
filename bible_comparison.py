import requests
from bs4 import BeautifulSoup
import re
import time

# Full pamphlet text here (copy-paste the exact text you provided)
pamphlet_text = """
MATTHEW
1:25 (FIRSTBORN) is omitted. (Speaking of the Lord Jesus.)
5:44 (BLESS THEM THAT CURSE YOU) is omitted.
6:13 (KINGDOM, POWER, GLORY) is omitted.
6.27 (STATURE) is changed to span of life.
6:33 (OF GOD) is omitted. (Referring to the kingdom)
8:29 (JESUS) is omitted. (As Son of God.)
9:13 (TO REPENTANCE) is omitted. CALLING SINNERS-
12:35 (OF THE HEART) is omitted. GOOD TREASURE-
12:47 (WHOLE VERSE) is omitted. (About Christ's mother.)
13:51 (JESUS SAID UNTO THEM and LORD) is omitted.
15:8 (DRAWETH UNTO ME WITH THEIR MOUTH) is omitted.
16:3 (O YE HYPOCRITES) is omitted.
16:20 (JESUS) is omitted.
17:21 (WHOLE VERSE) is omitted. (About prayer and fasting.)
18:11 (WHOLE VERSE) is omitted. (Tells Jesus came to save.)
19:9 (LAST 11 WORDS) are omitted. (About adultery.)
19:17 (GOD) is omitted. NONE GOOD BUT-
20:7 (WHATSOEVER IS RIGHT RECEIVE) is omitted.
20:16 (MANY BE CALLED BUT FEW CHOSEN) is omitted.
20:22 (BAPTIZED WITH CHRIST'S BAPTISM) is omitted.
21:44 (WHOLE VERSE) is omitted. (About Christ the stone.)
23:14 (WHOLE VERSE) is omitted. Woe Scribes and hypocrites.)
25:13 (WHEREIN THE SON OF MAN COMETH) is omitted.
27:35 (FULFILLED SPOKEN BY THE PROPHET) is omitted.
27:54 (THE son of God) is changed to A son of God.
28:2 (FROM THE DOOR) is omitted.
28:9 (THEY WENT TO TELL HIS DISCIPLES) is omitted.

MARK
1:1 (SON OF GOD) is omitted from some versions.
1:14 (OF THE KINGDOM) is omitted. Jesus gospel-
1:31 (IMMEDIATELY) is omitted. THE FEVER LEFT-
2:17 (TO REPENTANCE) is omitted. Call sinners -
6:11 (MORE TOLERABLE FOR SODOM & GOMORRAH) is omitted.
6:16 (FROM THE DEAD) is omitted, JOHN IS RISEN-
6:33 (HIM) is changed to THEM.
7:8 (WASHING OF POTS AND CUPS) is omitted.
7:16 (WHOLE VERSE) is omitted. (About having an ear to hear.)
9:24 (LORD) is omitted. (A believer called Him Lord.)
9:42 (IN ME) is omitted. LITTLE ONES THAT BELIEVE-
9:44 (WHOLE VERSE) is omitted. (About fire not quenched.)
9:46 (WHOLE VERSE) is omitted. (Where the worm dieth not.)
9.49 (EVERY SACRIFICE SHALL BE SALTED) is omitted.
10:21 (TAKE UP THE CROSS) is omitted. JESUS SAID,-
10:24 (FOR THEM THAT TRUST IN RICHES) is omitted.
11:10 (IN THE NAME OF THE LORD) is omitted.
11:26 (WHOLE VERSE) is omitted. If ye do not forgive, etc.
13:14 (SPOKEN BY DANIEL THE PROPHET) is omitted.
13:33 (AND PRAY) is omitted, or in italics.
14.68 (AND THE COCK CREW) is omitted.
15:28 (WHOLE VERSE) is omitted. Scripture was fulfilled, etc.
15:39 (THE SON OF GOD) is a son of God.
16:9-20 (12 VERSES) are omitted. Some Bibles

LUKE
1:28 (BLESSED ART THOU AMONG WOMEN) is omitted.
2:33 (JOSEPH) is changed to FATHER.
2:43 (JOSEPH AND HIS MOTHER) is changed to PARENTS.
4:4 (BUT BY EVERY WORD OF GOD) is omitted.
4.8 (GET THEE BEHIND ME SATAN) is omitted.
4:41 (CHRIST) is omitted. -THE SON OF GOD.
6:48 (FOUNDED UPON A ROCK) is changed to WELL BUILT.
7:31 (AND THE LORD SAID) is omitted.
9:54 (EVEN AS ELIJAH DID) is omitted.
9:55 (YE KNOW NOT WHAT MANNER OF SPIRIT) is omitted.
9:56 (SON OF MAN IS COME TO SAVE LIVES) is omitted.
11:24 (MUCH OF THE LORD'S PRAYER) is omitted.
11:29 (THE PROPHET) is omitted. (About Jonah.)
17:36 (WHOLE VERSE) is omitted. (One taken, another left.)
21:4 (CAST IN UNTO THE OFFERINGS OF GOD) is omitted.
22:20 (WHOLE VERSE) is omitted from some versions.
22:31 (AND THE LORD SAID) is omitted.
22:64 (THEY STRUCK HIM ON THE FACE) is omitted.
23:17 (WHOLE VERSE) is omitted from many versions.
23:38 (LETTERS OF GREEK, LATIN, HEBREW) is omitted.
23:42 (LORD,) is omitted. -REMEMBER ME WHEN ...
23:45 (SUN WAS ECLIPSED) in Moffatt and NEB.
24:3 (OF THE LORD JESUS) is omitted.
24:6 (HE IS NOT HERE, BUT IS RISEN) is omitted.
24:12 (WHOLE VERSE) is omitted. (Peter's testimony.)
24:40 (WHOLE VERSE) is omitted. (Christ showed them hands, feet.)
24:49 (OF JERUSALEM) is omitted.
24:51 (CARRIED UP INTO HEAVEN) is omitted.

JOHN
1:14 (BEGOTTEN) is omitted from 1:18, 3:16, 3:18.
1:27 (PREFERRED BEFORE ME) is omitted. (Jesus is)
3:13 (WHICH IS IN HEAVEN) is omitted.
3:15 (SHOULD NOT PERISH) is omitted.
4:42 (THE CHRIST) is omitted.
5:3 (WAITING FOR MOVING OF THE WATER) is omitted.
5:4 (WHOLE VERSE) is omitted. (Regarding the Pool of Bethesda.)
6:17 (ON ME) is omitted. HE THAT BELIEVES-
6:69 (THAT CHRIST THE SON) is omitted.
7:53 (TO 8:11) is omitted, in brackets or italics.
8:16 (FATHER) is omitted. Changed to HE.
9:35 (SON OF GOD) is omitted, or changed to SON OF MAN.
11:41 (WHERE THE DEAD WAS LAID) is omitted.
16.16 (BECAUSE I GO TO THE FATHER) is omitted.
17:12 (IN THE WORLD) is omitted.
20:29 (THOMAS) is omitted.

ACTS
2:30 (ACCORDING TO FLESH RAISE UP CHRIST) is omitted.
7:30 (OF THE LORD) is omitted. AN ANGEL-
7:37 (HIM SHALL, YE HEAR) is omitted. (Speaking of Christ)
8:37 (WHOLE VERSE) is omitted, or in brackets, or italics.
9:5-6 (MUCH OF VERSE) is omitted. (Concerning God's will.)
10:6 (WHAT THOU OUGHTEST TO DO) More is omitted.
15:18 (KNOWN UNTO GOD HIS WORKS) More is omitted.
16:31 (CHRIST) is omitted.
17:26 (BLOOD) is omitted.
20:25 (OF GOD) is omitted. THE KINGDOM-
20:32 (BRETHREN) is omitted.
23:9 (LET US NOT FIGHT AGAINST GOD) is omitted.
24:6-8 (MUCH OF VERSE) is omitted, in brackets or italics.
24:15 (OF THE DEAD) is omitted. RESURRECTION-
28:16 (HALF OF VERSE) is omitted, in italics or brackets.
28:29 (WHOLE VERSE) is omitted, in italics or brackets.

ROMANS
1:16 (OF CHRIST) is out or in italics, brackets.
1:29 (FORNICATION) is omitted.
5:2 (BY FAITH) is omitted from some versions.
8.1 (LAST 10 WORDS) are omitted, or in italics.
9:28 (IN RIGHTEOUSNESS) is omitted.
10:15 (OF PEACE) is omitted. GOSPEL-
10.17 (OF GOD) is omitted. CHRIST is substituted.
11:6 (LAST 18 WORDS) are omitted.
13:9 (SHALL NOT BEAR FALSE WITNESS) is omitted,
14:6 (15 WORDS) are omitted. (Regarding the day)
14:21 (OFFENDED, MADE WEAK) is omitted.
15:29 (OF THE GOSPEL) is omitted.
16:24 (WHOLE VERSE) is omitted, in italics or brackets.

1 CORINTHIANS
1:14 (I THANK GOD) is out in many versions.
5:7 (FOR US) is omitted. CHRIST SACRIFICED-
6:20 (LAST 7 WORDS) are omitted. (Your spirit, etc.)
7:5 (AND FASTING) is omitted. JOINED WITH PRAYER-
7:39 (BY THE LAW) is omitted. THE WIFE IS BOUND-
10:28 (THE EARTH IS THE LORD'S) and more, is omitted.
11:24 (TAKE EAT) is omitted. THIS IS MY BODY-
11:29 (LORD'S) is omitted (Referring to the body.)
15:47 (THE LORD) is omitted. -FROM HEAVEN
16:22 (JESUS CHRIST) is omitted.
16:23 (CHRIST) is omitted.

2 CORINTHIANS
4:6 (JESUS) is omitted.
4:10 (THE LORD) is omitted.
5:18 (JESUS) is omitted, or in italics.
11:31 (CHRIST) is omitted, or in italics.

GALATIANS
1:15 (GOD) is omitted.
3:1 (THAT YE SHOULD NOT OBEY TRUTH) is omitted.
3:17 (IN CHRIST) is omitted.
4:7 (THROUGH CHRIST) is omitted.
6:15 (IN CHRIST JESUS) is omitted.
6:17 (LORD) is omitted.

EPHESIANS
3:9 (BY JESUS CHRIST) is omitted. GOD CREATED-
3:14 (OF OUR LORD JESUS CHRIST) is omitted.
5:30 (OF HIS FLESH AND OF HIS BONES) is omitted.
6:.1 (IN THE LORD) is omitted. OBEY PARENTS-
6:10 (MY BRETHREN) is omitted.

PHILIPPIANS
3:16 (LET US MIND THE SAME THING) is omitted.

COLOSSIANS
1:2 (THE LORD JESUS CHRIST) is omitted.
1:14 (THROUGH HIS BLOOD) is omitted, or in italics.
1:28 (JESUS) is omitted.
2:11 (OF THE SINS OF) is omitted.
3:6 (SONS OF DISOBEDIENCE) is omitted.

1 THESSALONIANS
1:1 (FROM GOD OUR FATHER AND LORD JESUS) is omitted.
2:19 (CHRIST) is omitted.
3:11 (CHRIST) is omitted, or in italics.
3:13 (CHRIST) is omitted, or in italics.

2 THESSALONIANS
1:8 (CHRIST) is omitted, or in italics.
1 TIMOTHY
1:17 (WISE) is omitted from THE ONLY WISE GOD.
2:7 (IN CHRIST) is omitted, or in italics.
3:16 (GOD) is omitted. -MANIFEST IN THE FLESH.
4:12 (IN SPIRIT) is omitted.
6:5 (FROM SUCH WITHDRAW THYSELF) is omitted.
2 TIMOTHY
1:11 (OF THE GENTILES) is omitted.
4:1 (LORD) is omitted.
4:22 (JESUS CHRIST) is omitted, or in italics.

TITUS
1:4 (THE LORD) is omitted, or in italics.

PHILEMON
1:6 (JESUS) is omitted.
1:12 (RECEIVE HIM) is omitted.

HEBREWS
1:3 (BY HIMSELF) is omitted. -PURGED OUR SINS
2:7 (SET HIM OVER THE WORKS OF THY HANDS) is omitted.
3:1 (CHRIST) is omitted.
7:21 (AFTER ORDER OF MELCHIZEDEK) is omitted.
10:30 (SAITH THE LORD) is omitted.
10:34 (IN HEAVEN) is omitted.
11:11 (WAS DELIVERED OF A CHILD) is omitted. SARAH-

JAMES
5:16 (FAULTS) is changed to SINS. (Wrong Greek text.)

1 PETER
1:22 (THROUGH THE SPIRIT) is omitted.
4:1 (FOR US) is omitted. CHRIST SUFFERED-
4:14 (LAST 15 WORDS) are omitted, or in italics.
5:10 (JESUS) is omitted, or in italics.
5:11 (GLORY AND DOMINION) is omitted from some versions.

2 PETER
2:17 (FOREVER) is omitted, or in italics.
3:9 (US) is changed to YOU. (Destroys meaning.)

1 JOHN
1:7 (CHRIST) is omitted.
2:7 (FROM THE BEGINNING) is omitted.
4:3 (CHRIST IS COME IN THE FLESH) is omitted.
4:9 (BEGOTTEN) is omitted from some versions.
4:19 (HIM) is omitted, or in italics. WE LOVE-
5:7-8 (MANY WORDS) are omitted or changed.
5:13 (LAST 13 WORDS) are omitted.

JUDE
1:25 (WISE) is omitted. (Referring to God.)

REVELATION
1:8 (THE BEGINNING AND THE END) is omitted.
1:11 (TEN WORDS) are omitted. (Alpha and Omega, etc.)
2:13 (THY WORKS) is omitted.
5:14 (HIM THAT LIVETH FOREVER AND EVER) is omitted.
6:1,3,5,7 (AND SEE) is omitted.
8:13 (ANGEL) is changed to EAGLE. (Greek text says ANGEL.)
11:17 (AND ART TO COME) is omitted.
12:12 (INHABITERS OF) is omitted. -THE EARTH.
22:17 (CHRIST) is omitted.
14:5 (BEFORE THE THRONE OF GOD) is omitted.
16:17 (OF HEAVEN) is omitted.
20:9 (GOD OUT OF) is omitted. FIRE CAME FROM-
20:12 (GOD) is changed to THRONE
21:24 (OF THEM WHICH ARE SAVED) is omitted. NATIONS-
21:24 (OF THEM WHICH ARE SAVED) is omitted. NATIONS-
"""

bible_books = ['Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', 'Jude', 'Revelation']

def parse_entries(text):
    entries = []
    current_book = None
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    i = 0
    while i < len(lines):
        line = lines[i]
        upper = line.upper()
        book_match = None
        for b in bible_books:
            if upper == b.upper():
                book_match = b
                break
        if book_match:
            current_book = book_match
            i += 1
            continue
        
        if current_book:
            # Continue note from previous if no ref (for broken lines)
            if re.match(r'^\d+[:.\d-]', line):
                # New entry
                match = re.match(r'^(\d+[:.\d-]+\d*)\s*(.*)', line, re.I)
                if match:
                    ref = match.group(1).replace('.', ':').strip()
                    note = match.group(2).strip()
                    entries.append({'book': current_book, 'ref': ref, 'note': note})
                else:
                    # fallback
                    parts = line.split(' ', 1)
                    ref = parts[0].replace('.', ':')
                    note = parts[1] if len(parts) > 1 else ''
                    entries.append({'book': current_book, 'ref': ref, 'note': note})
            else:
                # Append to last note (for hyphenated breaks)
                if entries:
                    entries[-1]['note'] += ' ' + line
        i += 1
    return entries

entries = parse_entries(pamphlet_text)
print(f"Parsed {len(entries)} entries")  # Should be ~200

def get_verse_text(book, ref, version='KJV'):
    query = f"{book} {ref}"
    url = f"https://www.biblegateway.com/passage/?search={requests.utils.quote(query)}&version={version}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')

        # Target the actual verse text spans (most accurate)
        verse_spans = soup.find_all('span', class_=re.compile(r'text .*-\d+'))
        if verse_spans:
            # Remove footnotes/superscripts first
            for sup in soup.find_all('sup'):
                sup.decompose()

            # Critical fix: Use separator=' ' to preserve spaces between inline elements
            text_parts = [span.get_text(' ', strip=True) for span in verse_spans]
            full_text = ' '.join(text_parts)

            # Clean leading verse number and normalize spaces
            full_text = re.sub(r'^\d+\s*', '', full_text)
            full_text = re.sub(r'\s+', ' ', full_text).strip()

            return full_text if full_text else "(Omitted or not present)"

        # Fallback if no specific spans (rare, but for safety)
        passage = soup.find('div', class_=re.compile(r'passage'))
        if passage:
            for sup in passage.find_all('sup'):
                sup.decompose()
            text = passage.get_text(' ', strip=True)  # Also use separator here
            cutoff_keywords = ['Read full chapter', 'Passage Resources', 'Previous', 'Next', 'Add parallel', 'Share', 'Print', 'Listen', 'dropdown', 'Public Domain']
            for keyword in cutoff_keywords:
                if keyword in text:
                    text = text.split(keyword)[0]
            text = re.sub(r'^\d+\s*', '', text, count=1)
            text = re.sub(r'\s+', ' ', text).strip()
            return text if text else "(Omitted or not present)"

        return "(Not found)"

    except Exception as e:
        return f"(Error: {str(e)})"

# Group and generate
grouped = {}
for e in entries:
    grouped.setdefault(e['book'], []).append(e)

md = "# KJV vs Modern Versions: Missing/Changed Verses (per NEW EYE-OPENER)\n\n"
html = '<html><head><title>KJV Comparison</title><style>table{border-collapse:collapse;width:100%;}th,td{border:1px solid #ccc;padding:8px;text-align:left;vertical-align:top;}th{background:#f0f0f0;}</style></head><body><h1>KJV vs ESV vs NIV: Missing/Changed Verses</h1>'

for book, items in grouped.items():
    md += f"## {book}\n\n| Ref | Note | KJV | ESV | NIV |\n|---|----|-----|-----|-----|\n"
    html += f"<h2>{book}</h2><table><tr><th>Ref</th><th>Note</th><th>KJV</th><th>ESV</th><th>NIV</th></tr>"
    
    for item in items:
        time.sleep(0.8)  # Polite delay
        kjv = get_verse_text(item['book'], item['ref'], 'KJV')
        esv = get_verse_text(item['book'], item['ref'], 'ESV')
        niv = get_verse_text(item['book'], item['ref'], 'NIV')
        
        md += f"| {item['ref']} | {item['note']} | {kjv} | {esv} | {niv} |\n"
        html += f"<tr><td>{item['ref']}</td><td>{item['note']}</td><td>{kjv}</td><td>{esv}</td><td>{niv}</td></tr>"
    
    md += "\n"
    html += "</table><br>"

html += "</body></html>"

with open('kjv_comparison.md', 'w', encoding='utf-8') as f:
    f.write(md)
with open('kjv_comparison.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! Files: kjv_comparison.md and kjv_comparison.html")
