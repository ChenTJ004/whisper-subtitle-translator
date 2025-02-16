# 🎬 Whisper Subtitle Translator

本项目使用 OpenAI Whisper 进行自动字幕生成，并支持将字幕翻译成多种语言。🎯

## ✨ 功能
- 🗣️ 语音转文字（支持多语言）
- 🌍 字幕自动翻译（支持 Whisper 或 OpenAI API）
- 🎥 视频字幕嵌入

## 📥 安装
### 1️⃣ 克隆仓库
```bash
git clone https://github.com/your_username/whisper-subtitle-translator.git
cd whisper-subtitle-translator
```

### 2️⃣ 安装依赖
```bash
pip install -r requirements.txt
```

## 🏃 使用方法
### **1️⃣ 生成字幕**
```bash
python whisper_subtitle.py generate --video sample_video.mp4 --language it
```

### **2️⃣ 翻译字幕**
```bash
python whisper_subtitle.py translate --input sample_italian.srt --output translated.srt --target_lang en
```

## 📜 示例
| 原始意大利语字幕 | 翻译后英语字幕 |
|----------------|----------------|
| Ciao! Benvenuti nel nostro video. | Hello! Welcome to our video. |
| Oggi parleremo di come creare i sottotitoli automaticamente. | Today we will talk about how to create subtitles automatically. |

## 🎥 将字幕嵌入视频
可以使用 **HandBrake** 进行嵌入：
1. 打开 **HandBrake**，导入 `sample_video.mp4`
2. 选择 **“Subtitles” → “Import SRT”**，导入 `translated.srt`
3. 勾选 **“Burn In”**，然后导出新视频。

## 🤝 贡献
欢迎提交 PR 或 issue 进行优化！🚀

