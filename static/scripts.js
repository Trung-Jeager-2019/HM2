// Hiển thị nút khi người dùng cuộn xuống
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    const backToTopButton = document.getElementById("backToTop");
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        backToTopButton.style.display = "block"; // Hiển thị nút khi lăn quá 300px
    } else {
        backToTopButton.style.display = "none"; // Ẩn nút khi ở trên cùng
    }
}

// Lăn lên đầu trang khi nhấp vào nút
document.getElementById("backToTop").addEventListener("click", function(event) {
    event.preventDefault();
    window.scrollTo({top: 0, behavior: 'smooth'}); // Lăn lên đầu trang với hiệu ứng mượt
});



// Lấy các trường "Từ", "Đến", và "Loại xe"
var fromInput = document.getElementById('from');
var toInput = document.getElementById('to');
var vehicleSelect = document.getElementById('vehicle');

// Lấy phần tử hiển thị ảnh loading và giá
var loadingElement = document.getElementById('loading'); // Phần tử cho ảnh loading
var priceElement = document.getElementById('price');
var priceDisplay = document.getElementById('price-display');

// Thời gian hiển thị loading (3 giây)
var timeout;

// Kiểm tra khi thay đổi các trường
function updatePrice() {
    var fromValue = fromInput.value.trim();
    var toValue = toInput.value.trim();
    var vehicleType = vehicleSelect.value;

    // Nếu đang có timeout trước đó, hãy xóa nó
    if (timeout) {
        clearTimeout(timeout);
    }

    // Nếu cả ba trường đều đã được nhập
    if (fromValue !== "" && toValue !== "" && vehicleType !== "") {
        // Hiển thị ảnh loading và ẩn giá
        loadingElement.style.display = 'inline-block'; // Hiển thị ảnh loading
        priceDisplay.style.display = 'none'; // Ẩn giá trong lúc loading

        // Đặt timeout để hiển thị giá sau 3 giây
        timeout = setTimeout(function() {
            var price = 0;

            // Random giá dựa trên loại xe đã chọn
            if (vehicleType === 'ba_gac') {
                price = Math.floor(Math.random() * (200000 - 100000 + 1)) + 100000;
            } else if (vehicleType === 'xe_tai_nho') {
                price = Math.floor(Math.random() * (300000 - 200000 + 1)) + 200000;
            } else if (vehicleType === 'xe_tai_trung') {
                price = Math.floor(Math.random() * (400000 - 300000 + 1)) + 300000;
            }

            if (price > 0) {
                priceElement.textContent = price.toLocaleString('vi-VN') + ' đ';
                priceDisplay.style.display = 'block'; // Hiển thị giá
            }

            // Ẩn ảnh loading
            loadingElement.style.display = 'none';
        }, 2000); // Hiện giá sau 3 giây
    } else {
        priceDisplay.style.display = 'none'; // Ẩn giá nếu chưa nhập đủ thông tin
        loadingElement.style.display = 'none';  // Ẩn ảnh loading nếu chưa nhập đủ
    }
}

// Lắng nghe sự kiện thay đổi trên cả ba trường
fromInput.addEventListener('input', updatePrice);
toInput.addEventListener('input', updatePrice);
vehicleSelect.addEventListener('change', updatePrice);






