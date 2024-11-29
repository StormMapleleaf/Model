document.getElementById('draw-button').onclick = function() {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '正在抽奖，请稍候...';

    fetch('/draw')
        .then(response => response.json())
        .then(data => {
            let resultHtml = '<h2>抽奖结果</h2>';
            for (const school in data) {
                resultHtml += `<h3>${school}</h3>`;
                resultHtml += '<h4>男生:</h4><ul>';
                data[school]['男生'].forEach(student => {
                    resultHtml += `<li>${student[1]} - 学号: ${student[3]}</li>`;
                });
                resultHtml += '</ul><h4>女生:</h4><ul>';
                data[school]['女生'].forEach(student => {
                    resultHtml += `<li>${student[1]} - 学号: ${student[3]}</li>`;
                });
                resultHtml += '</ul>';
            }
            resultDiv.innerHTML = resultHtml;
        })
        .catch(error => {
            resultDiv.innerHTML = '抽奖失败，请重试。';
            console.error('Error:', error);
        });
};
