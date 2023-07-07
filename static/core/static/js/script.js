document.addEventListener("DOMContentLoaded", function() {
  const letterLinks = document.querySelectorAll(".letter-link");
  const clearButton = document.getElementById("clearButton");
  const searchInput = document.getElementById("searchInput");

  letterLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      event.preventDefault();
      const letter = this.getAttribute("data-letter");
      showMedicationsByLetter(letter);
    });
  });

  clearButton.addEventListener("click", function(event) {
    event.preventDefault();
    alert("Button clicked");
    clearAllContent();
  });

  searchInput.addEventListener("input", function() {
    const query = this.value.toLowerCase();
    const rows = document.querySelectorAll(".table-container tbody tr");

    rows.forEach(function(row) {
      const name = row.cells[1].innerText.toLowerCase();
      const activeIngredient = row.cells[2].innerText.toLowerCase();
      const isVisible = name.includes(query) || activeIngredient.includes(query);
      row.style.display = isVisible ? "table-row" : "none";
    });

    const tableContainers = document.querySelectorAll(".table-container");
    tableContainers.forEach(function(container) {
      const visibleRows = container.querySelectorAll("tbody tr[style='display: table-row;']");
      container.style.display = visibleRows.length > 0 ? "block" : "none";
    });

    clearSelectedLetter();
  });

  function showMedicationsByLetter(letter) {
    const tableContainers = document.querySelectorAll('[id$="-table-container"]');
    tableContainers.forEach(function(container) {
      container.style.display = container.id === `${letter}-table-container` ? "block" : "none";
    });

    clearSearchInput();
  }

  function clearSearchInput() {
    document.getElementById("searchInput").value = "";
  }


  function clearSelectedLetter() {
    const selectedLetterContainer = document.querySelector(".letter-container:not([style*='display: none'])");
    if (selectedLetterContainer) {
      const tableContainer = selectedLetterContainer.querySelector(".table-container");
      tableContainer.style.display = "none";
    }
  }


  function togglePurpose(id) {
    const dots = document.getElementById("dots" + id);
    const moreText = document.getElementById("more" + id);
    const moreLink = document.getElementById("moreLink" + id);

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      moreText.style.display = "none";
      moreLink.innerHTML = "More";
    } else {
      dots.style.display = "none";
      moreText.style.display = "inline";
      moreLink.innerHTML = "Less";
    }
    clearSearchInput();
  }
});
