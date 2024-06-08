function gotodep() {
    window.location.href = "department.html";
  }
  function information_hospitals() {
    window.location.href = "information_hospitals.html";
  }
  function archive_medcards() {
    window.location.href = "archive_medcards.html";
  }
  function analyzes(id) {
window.location.href = "analyzs.html?id=" + id;
}
  function inspections(id) {
    window.location.href = "inspections.html?id=" + id;
  }
  function diaries(id) {
    window.location.href = "diaries.html?id=" + id;
  }
  function diagnoses(id) {
    window.location.href = "diagnoses.html?id=" + id;
  }

  function showContent(contentId) {
    document.querySelectorAll(".content1, .content2").forEach((content) => {
      content.classList.remove("active");
    });
    document.getElementById(contentId).classList.add("active");

    document.querySelectorAll(".btn_block2").forEach((button) => {
      button.classList.remove("active");
    });
    document
      .querySelector(`[onclick="showContent('${contentId}')"]`)
      .classList.add("active");
  }

  const buttons = document.querySelectorAll(".btn_block2");
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      buttons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");
    });
  });
  function toggleDropdown1(id) {
    var dropdown = document.getElementById(id);
    dropdown.style.display =
      dropdown.style.display === "flex" ? "none" : "flex";
  }

  function showContent(contentId) {
    document.querySelectorAll(".content1, .content2").forEach((content) => {
      content.classList.remove("active");
    });
    document.getElementById(contentId).classList.add("active");

    document.querySelectorAll(".btn_block2").forEach((button) => {
      button.classList.remove("active");
    });
    document
      .querySelector(`[onclick="showContent('${contentId}')"]`)
      .classList.add("active");
  }

  function showContent2(option) {
    document.getElementById("content11").style.display =
      option == 1 ? "block" : "none";
    document.getElementById("content12").style.display =
      option == 2 ? "block" : "none";
  }
    // Функция для открытия модального окна
function openPopup(id) {
var popup = document.getElementById(id);
if (popup) {
  popup.style.display = "block";
}
}

// Функция для закрытия модального окна
function closePopup(id) {
var popup = document.getElementById(id);
if (popup) {
  popup.style.display = "none";
}
}

document.addEventListener('DOMContentLoaded', function() {
const dropdownToggle = document.querySelector('.dropdown-toggle');
const dropdownMenu = document.querySelector('.dropdown-menu');
const doctorIcon = document.querySelector('.doctor');

dropdownToggle.addEventListener('click', function(event) {
    event.preventDefault();
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', function(event) {
    if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = 'none';
    }
});
});
