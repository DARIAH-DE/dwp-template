---
title: Emma 
author:
- Jane Austen
- Mirjam Blümm
longauthor:
- Jane Austen¹
- Mirjam Blümm²
institute: 
- ¹Winchester
- ²SUB Göttingen
lang: en
report-number: 123
abstract: |
        Emma, by Jane Austen is a novel about youthful hubris and the perils of
        misconstrued romance. 
        
        As in her other novels, Austen explores the concerns and difficulties
        of genteel women living in Georgian-Regency England; she also creates
        a lively comedy of manners among her characters. 
keywords-en: 
- Austen
- novel
- England 
keywords-de: 
- Austen
- Roman
- England 
date: 1816
wpno: 4711
...

# Micro Typography

There are various ways to include smart typography: If you take quotes, for example, you can use "straight" quotes, ``LaTeX-style'' quotes or “proper unicode quotes”, let's see what happens when someone uses «inverse French», »French« or „German“ quotes in an otherwise English text.

Dashes are also important. Here's a hyphen-esque situation — immediately followed by a unicode em-dash that has been properly surrounded with unicode thin spaces. Now ASCII hyphens---three of them. You might also try an en-dash: Here – the Unicode variant, surrounded by spaces, and now -- the two-hyphen variant, also surrounded by spaces.

Finally--two hyphens, no spaces.


# Languages and scientific components of text

If your text contains parts in a foreign language, use HTML-like tags like `<div lang="de">` to start and `</div>` to end. This will adapt hyphenation patterns and switch the quoting style:

<div lang="de">

Schon Pythargoras wußte, dass in einem rechtwinkligen Dreiek mit den "Ankatheten" $a$ und $b$ und der Hypothenuse $c$ gilt:

$$a^2 + b^2 = c^2 \iff c = \sqrt{a^2 + b^2}$$

Man müsste jetzt noch [Aussagen](http://de.wikipedia.org/Aussage) über die Winkel $\alpha, \beta, \gamma$ etc. machen.

</div>

Code snippets can be included in the text, but also as separate blocks. Denote the programming language to get syntax highlighting:

```haskell
quicksort [] = []
quicksort (p:xs) = (quicksort lesser) ++ [p] ++ (quicksort greater)
    where
        lesser = filter (< p) xs
        greater = filter (>= p) xs
```

# Citations

It is easily possible to include references [@hh2010]. To do so we recommend the following:

1. Write or export your bibliography as a BibLaTeX database named alike your article – i. e. for `test.md`, it should be called `test.bib`.
2. End your markdown document with a line that reads `\bibliography`.

References to your bibliography can be written in a number of ways:

* Easiest way is to write `[@hh2010]` [@hh2010]. 
* You can also include prefixes and page references as in `[see @hh2010, p. 1]` [see @hh2010, p. 1].
* Text references look like @hh2010a, without the brackets: `@hh2010a`
* Multiple references share brackets [see, e. g., @hh2010; @hh2010a; @hh2010b]
* "As Hagen [-@hh2010] says" is a common beginning for which the author of a citation can be suppressed

# Introduction 

 Emma (Austen 1815) QUELLENANGABE ^[Quellenagaben im Text in Klammern einfügen (Autor, Jahr, ggf. Seitenangabe)], by Jane Austen is a novel about youthful hubris and the perils of misconstrued romance. As in her other novels, Austen explores the concerns and difficulties of genteel women living in Georgian-Regency England; she also creates a lively comedy of manners among her characters.^[<https://en.wikipedia.org/wiki/Emma_(novel)> SELFLINKED LINKS, Links möglichst in die Fußnoten setzen ] FOOTNOTE

| Emma Woodhouse | Harriett Smith | Mr. George Knightley  | Mr. Woodhouse |
| :------------- | :------------- |  -------------------: | -------------:|
| Protagonist    | Emmas protegé  | Brother in Law        | Father        |



# Chapter One HEADING 1 


## Emma Woodhouse HEADING 2 


Emma Woodhouse, handsome, clever, and rich, with a comfortable home and happy disposition, seemed to unite some of the best blessings of existence; and
had lived nearly twenty-one years in the world with very little to distress or vex her. TEXT BODY

1. She was the youngest of the two daughters of a most affectionate, indulgent father; LIST AND NUMBERING
2. And had, in consequence of her sister's marriage, been mistress of his house from a very early period.
3. Her mother had died too long ago for her to have more than an indistinct remembrance of her caresses, and her place had been supplied by an excellent woman as governess, who had fallen little short of a mother in affection.

![BILDUNTERSCHRIFT ](img/Logo_Working-Papers.pdf)

Sixteen years had Miss Taylor been in Mr. Woodhouse's family, less as a governess than a friend, very fond of both daughters, but particularly of Emma. Between them it was more the intimacy of sisters.

> Even before Miss Taylor had ceased to hold the nominal office of governess, the mildness of her temper had hardly allowed her to impose any restraint; and the shadow of authority being now long passed away, they had been living together as friend and friend very mutually attached, and Emma doing just what she liked; highly esteeming Miss Taylor's judgment, but directed chiefly by her own. BLOCKQUOTE 


### How was she to bear the change? HEADING 3 


How was she to bear the change?--It was true that her friend was going only half a mile from them;

- but Emma was aware that great must be the difference between a Mrs. Weston, only half a mile from them, and a Miss Taylor in the house; (LIST AND BULLET POINTS)
- and with all her advantages, natural and domestic, she was now in great danger of suffering from intellectual solitude.

She dearly loved her father, but he was no companion for her. He could not meet her in conversation, rational or playful.


# List of Abbreviations


- E – Emma (LIST AND BULLET POINTS)
- JA – Jane Austen


\biblio


Austen-Leigh, James Edward. 1967. A Memoir of Jane Austen. Ed. R. W. Chapman. Oxford: Oxford University Press. (Bibliography)

Todd, Janet. 2006. The Cambridge Introduction to Jane Austen. Cambridge University Press.

Mazmanian, Melissa. 1999. "Reviving Emma". Persuasions Online 3/2, 12-34.


