from flask import Flask, render_template, request


app = Flask(__name__)

# Tạo một danh sách các từ vựng và ý nghĩa tương ứng
vocab_list = [
    {'vocab': 'cat', 'meaning': 'con mèo'},
    {'vocab': 'dog', 'meaning': 'con chó'},
    {'vocab': 'bird', 'meaning': 'con chim'}
]

# Định nghĩa route ban đầu khi trang web được mở
@app.route('/')
def index():
    # Lấy chỉ số từ vựng đầu tiên
    index = 0
    return render_template('flashcard.html', vocab=vocab_list[index]['vocab'], meaning=vocab_list[index]['meaning'])

# Định nghĩa chức năng next
@app.route('/next', methods=['POST'])
def next():
    # Lấy chỉ số hiện tại từ form
    current_index = int(request.form.get('current_index'))
    if current_index < len(vocab_list) - 1:
        # Chuyển tới từ vựng tiếp theo nếu có
        next_index = current_index + 1
    else:
        # Quay trở lại từ vựng đầu tiên nếu đã đến cuối danh sách từ vựng
        next_index = 0
    return render_template('flashcard.html', vocab=vocab_list[next_index]['vocab'], meaning=vocab_list[next_index]['meaning'])

# Định nghĩa chức năng back to home
@app.route('/back_to_home')
def back_to_music():
    # Mã xử lý để quay trở lại trang chủ
    return "Quay trở lại trang chủ"

if __name__ == '__main__':
    app.run(debug= True)
