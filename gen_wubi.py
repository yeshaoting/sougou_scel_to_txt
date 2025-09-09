#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pywubi import wubi
from collections import defaultdict

def generate_wubi_codes():
    """生成五笔编码"""
    # 检查词汇文件是否存在
    words_file = "./output/words.txt"
    if not os.path.exists(words_file):
        print(f"错误：词汇文件 {words_file} 不存在")
        print("请先运行 scel_to_txt.py 和 merge_txt.py 生成词汇文件")
        return
    
    # 读取词汇文件
    try:
        with open(words_file, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print(f"读取词汇文件时出错: {e}")
        return
    
    # 创建五笔编码映射字典
    wubi_dict = defaultdict(list)
    failed_words = []
    
    print(f"开始处理 {len(words)} 个词汇...")
    
    # 处理每个词汇
    for i, word in enumerate(words, 1):
        try:
            # 生成五笔编码（使用词组模式）
            wubi_codes = wubi(word, single=False)
            
            # pywubi返回列表，取第一个编码作为键
            if wubi_codes and len(wubi_codes) > 0:
                wubi_code = wubi_codes[0]
                # 将词汇添加到对应编码的列表中
                wubi_dict[wubi_code].append(word)
            else:
                print(f"无法生成词汇 '{word}' 的五笔编码: 无有效编码")
                failed_words.append(word)
            
            if i % 100 == 0:
                print(f"已处理 {i}/{len(words)} 个词汇")
                
        except Exception as e:
            print(f"无法生成词汇 '{word}' 的五笔编码: {e}")
            failed_words.append(word)
    
    # 输出失败词汇
    if failed_words:
        print(f"\n无法生成五笔编码的词汇 ({len(failed_words)} 个):")
        for word in failed_words:
            print(f"  {word}")
    
    # 写入结果文件
    output_file = "./output/wubi.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for code, word_list in wubi_dict.items():
                # 五笔编码在前，多个词汇用空格隔开
                words_str = ' '.join(word_list)
                f.write(f"{code} {words_str}\n")
        
        print(f"\n处理完成！结果已保存到 {output_file}")
        print(f"成功处理词汇: {len(words) - len(failed_words)} 个")
        print(f"失败词汇: {len(failed_words)} 个")
        
    except Exception as e:
        print(f"写入结果文件时出错: {e}")

if __name__ == "__main__":
    generate_wubi_codes()