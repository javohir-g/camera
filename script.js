function domReady(fn) {
    if (
        document.readyState === "complete" ||
        document.readyState === "interactive"
    ) {
        setTimeout(fn, 1000);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

domReady(function () {
    const tg = window.Telegram.WebApp; // Mini App API

    function onScanSuccess(decodeText, decodeResult) {
        console.log("QR-код найден:", decodeText);

        // Отправляем данные в бота
        tg.sendData(decodeText);

        // Показываем пользователю результат
        alert("QR-код: " + decodeText);
    }

    let htmlscanner = new Html5QrcodeScanner(
        "my-qr-reader",
        { fps: 10, qrbox: 250 }
    );

    htmlscanner.render(onScanSuccess);
});
