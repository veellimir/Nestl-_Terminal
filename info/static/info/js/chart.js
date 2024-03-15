// ASSEMBLY STANDARD
const totalCollectedElement = document.querySelector('.chart_collected p'),
      currentQuantity = document.querySelector('.chart_collected'),
      assemblingElement = document.querySelector('.task_assembling'),
      result = document.querySelector('.all_style_chart p')

let totalCollected = parseInt(totalCollectedElement.textContent),
    assembling = parseInt(assemblingElement.textContent);

function updateChart(total, assembling) {
    totalCollected = total;

    const percentage = (totalCollected / assembling) * 100,
          height = (percentage / 100) * 300;

    currentQuantity.style.height = height + 'px';

    if (percentage >= 50 && percentage < 70) {
        currentQuantity.style.backgroundColor = '#FFD700';
    } else if (percentage >= 70) {
        currentQuantity.style.backgroundColor = '#00FF00';
    } else {
        currentQuantity.style.backgroundColor = '#8B0000';
    }
    result.textContent = `${totalCollected} кор. ${percentage.toFixed(0)}%`;
}

const newTotalCollected = parseInt(totalCollectedElement.textContent);
totalCollectedElement.textContent = newTotalCollected;

updateChart(newTotalCollected, assembling);

