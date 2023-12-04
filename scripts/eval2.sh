python llava/eval/eval_gpt_review_visual2.py \
    --question playground/data/coco2014_val_qa_eval/qa90_questions.jsonl \
    --context llava/eval/table/caps_boxes_coco2014_val_80.jsonl \
    --answer-list \
    playground/data/coco2014_val_qa_eval/qa90_gpt4_answer.jsonl \
    $1 \
    --rule llava/eval/table/rule.json \
    --output vqa/reviews/coco2014_val80/gpt4_text_${2}.jsonl