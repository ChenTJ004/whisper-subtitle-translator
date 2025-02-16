import argparse
import whisper
import openai


def generate_subtitles(video_path, language="auto"):
	model = whisper.load_model("medium")  # 选择模型（"small", "medium", "large"）
	result = model.transcribe(video_path, language=language)

	srt_path = video_path.replace(".mp4", ".srt")
	with open(srt_path, "w", encoding="utf-8") as f:
		for i, segment in enumerate(result["segments"]):
			start = segment["start"]
			end = segment["end"]
			text = segment["text"]
			f.write(f"{i + 1}\n{format_time(start)} --> {format_time(end)}\n{text}\n\n")

	print(f"✅ 字幕已生成: {srt_path}")


def format_time(seconds):
	""" 将秒转换为字幕格式 00:00:00,000 """
	millisec = int((seconds - int(seconds)) * 1000)
	return f"{int(seconds // 3600):02}:{int((seconds % 3600) // 60):02}:{int(seconds % 60):02},{millisec:03}"


def translate_text(text, target_lang="en"):
	""" 使用 OpenAI GPT 翻译文本 """
	response = openai.ChatCompletion.create(
		model="gpt-4",
		messages=[{"role": "system", "content": f"Translate this text to {target_lang}:"},
				  {"role": "user", "content": text}]
	)
	return response["choices"][0]["message"]["content"]


def translate_srt(input_srt, output_srt, target_lang="en"):
	""" 读取 SRT 文件并翻译 """
	with open(input_srt, "r", encoding="utf-8") as f:
		lines = f.readlines()

	translated_lines = []
	for line in lines:
		if line.strip() and not line[0].isdigit():  # 只翻译字幕内容
			translated_lines.append(translate_text(line, target_lang) + "\n")
		else:
			translated_lines.append(line)

	with open(output_srt, "w", encoding="utf-8") as f:
		f.writelines(translated_lines)

	print(f"✅ 翻译完成: {output_srt}")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest="command")

	parser_sub = subparsers.add_parser("generate")
	parser_sub.add_argument("--video", required=True, help="视频文件路径")
	parser_sub.add_argument("--language", default="auto", help="字幕语言 (默认自动检测)")

	parser_trans = subparsers.add_parser("translate")
	parser_trans.add_argument("--input", required=True, help="输入 SRT 文件")
	parser_trans.add_argument("--output", required=True, help="输出翻译后的 SRT 文件")
	parser_trans.add_argument("--target_lang", default="en", help="目标语言 (默认英语)")

	args = parser.parse_args()

	if args.command == "generate":
		generate_subtitles(args.video, args.language)
	elif args.command == "translate":
		translate_srt(args.input, args.output, args.target_lang)
