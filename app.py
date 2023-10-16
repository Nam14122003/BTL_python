from django.shortcuts import render
from django.http import HttpResponse

# Tạo một danh sách các từ vựng và ý nghĩa tương ứng
vocab_list = [
    {'vocab': 'cat', 'meaning': 'con mèo'},
    {'vocab': 'dog', 'meaning': 'con chó'},
    {'vocab': 'bird', 'meaning': 'con chim'}
]

# Định nghĩa view ban đầu khi trang web được mở
def index(request):
    # Lấy chỉ số từ vựng đầu tiên
    index = 0
    return render(request, 'flashcard.html', {'vocab': vocab_list[index]['vocab'], 'meaning': vocab_list[index]['meaning'], 'current_index': index})

# Định nghĩa chức năng next
def next(request):
    # Lấy chỉ số hiện tại từ request.POST
    current_index = int(request.POST.get('current_index'))
    if current_index < len(vocab_list) - 1:
        # Chuyển tới từ vựng tiếp theo nếu có
        next_index = current_index + 1
    else:
        # Quay trở lại từ vựng đầu tiên nếu đã đến cuối danh sách từ vựng
        next_index = 0
    return render(request, 'flashcard.html', {'vocab': vocab_list[next_index]['vocab'], 'meaning': vocab_list[next_index]['meaning'], 'current_index': next_index})

# Định nghĩa chức năng back to home
def back_to_home(request):
    # Mã xử lý để quay trở lại trang chủ
    return HttpResponse("Quay trở lại trang chủ")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
