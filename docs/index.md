---
layout: base
title:  'RANIS - Relational representation of context-dependent roles on information science papers'
---

# RANIS - Relational representation of context-dependent roles on information science papers

[GitHub repository](https://github.com/mynlp/ranis)

as of 2017-08-28

This corpus is a set of research abstracts in information science domain, where the mentions of named entities and domain specific entites are marked and their roles in the context of the paper are annotated in the form of relations to other entities.
There are two subcorpora: the Japanese corpus consisting of 230 abstracts from IPSJ (Information Procsssing Society of Japan) Journal, and the English corpus consisting of 250 abstracts from the ACL anthology and 150 abstracts from SEMEVAL 2010 task5 set (part of the ACM digital library).

The corpus is created using [brat](http://brat.nlplab.org/) and the annotation is in the brat standoff format (see <http://brat.nlplab.org/standoff.html>). The configuration files for viewing with brat is also included in corpus.  

## Japanese Corpus

The following files are included, in the JA subdirectory:

* data
    * goldstandard-v2:    
    The version mentioned in [LAW](https://aclweb.org/anthology/W/W13/W13-2318.pdf) and [LREC](http://www.lrec-conf.org/proceedings/lrec2014/pdf/461_Paper.pdf) papers.

        * dev:
	      Reference set, 100 abstracts

        * test: Test set,30 abstracts

    * dev2: Additional set, 100 abstracts

* MetaData.tsv.txt:
	The [Johogaku-Hiroba](https://ipsj.ixsq.nii.ac.jp/) IDs for the abstracts in TSV.

## English Corpus

The following files are included, in the EN subdirectory:

* data
    * original: Original annotation
        * dev: Reference set
            * ACL: From ACL Anthology (230 abstracts)
            * ACM: From ACM Digital Library (130 abstracts)
        * test: Test set
            * ACL: From ACL Anthology (20 abstracts)
            * ACM: From ACM Digital Library (20 abstracts)
* Gupta.list
	A plain text file containing the list of IDs used for Extraction of Focus, Domain, Technique described in the LREC-16 paper.

The annotation scheme for the English data is more fine-grained than the scheme for the Japanese data, and the former can be converted into the latter.  The [conversion script](https://github.com/mynlp/ranis/blob/master/scripts/convert_v2_to_v1.py) is available.

## Documentation

Annotation guidelines for Japanese and English data are available.

* [Japanese corpus](http://mynlp.github.io/ranis/JA/manual.pdf) (PDF)
* [English corpus](http://mynlp.github.io/ranis/EN/) (HTML)

## Notes

When you publish the results using the Japanese corpus, please cite

* Yuka Tateisi,Yo Shidahara,Yusuke Miyao,Akiko Aizawa.
  Annotation of Computer Science Papers for Semantic Relation Extraction.
  Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC-2014).
  pp.1423-1429.
  Reykjavik, Iceland.
  May 26-31, 2014. [PDF at LREC site](http://www.lrec-conf.org/proceedings/lrec2014/pdf/461_Paper.pdf)

When you publish the results using the Japanese corpus, please cite
* Yuka Tateisi, Tomoko Ohta, Sampo Pyysalo, Yusuke Miyao and Akiko Aizawa
  Typed Entity and Relation Annotation on Computer Science Papers.
  Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC-2016).
  pp.3836-3843.
  Portorož, Slovenia.
  [PDF at LREC site](http://www.lrec-conf.org/proceedings/lrec2016/pdf/784_Paper.pdf)

This work was partially supported by JSPS Grant-in-Aid for Scientific Research (B) No. 22300031, and by Data Centric Science Research Commons.

Annotations are Copyright (C) 2013-2016 Miyao Lab, National Institute of Informatics, Japan
![Creative Commons License CC-BY-SA](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)

IPSJ materials are Copyright (C) 1960-2016 Information Processing Society of Japan; ACL materials are Copyright (C) 1963-2016 ACL; other materials are copyrighted by their respective copyright holders. 


