# Winograd-Schema-Challenge-Ja
Japanese Translation of Winograd Schema Challenge (http://www.hlt.utdallas.edu/~vince/data/emnlp12/)

## Dataset
- train: train.txt (1,322 tasks)
- test:  test.txt  (  564 tasks)

### Format
- Five lines correspond to one task, which consists of the following four lines (and one blank line).
```
input sentence(s)     Japanese translation (comments if any)
target pronoun     Japanese translation
antecedent candidates Japanese translation
correct antecedent     Japanese translation
```   
- Example:
```
"James asked Robert for a favor, but he refused."       ジェームズはロバートに頼みごとをした。しかし彼は断った。                
he      彼                              
"James,Robert"  ジェームズ、　ロバート                          
Robert  ロバート 
```

## Dataset Reader
```bash
$ python winograd_schema_challenge_ja_reader.py --train_file train.txt --test_file test.txt
```

## History
- 0.1
    - initial commit

## Reference
柴田知秀, 小浜翔太郎, 黒橋禎夫:
日本語Winograd Schema Challengeの構築と分析.
言語処理学会 第21回年次大会 (2015.3) (in Japanese). 
http://www.anlp.jp/proceedings/annual_meeting/2015/pdf_dir/E3-1.pdf
