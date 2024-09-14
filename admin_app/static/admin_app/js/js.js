 // Get filter elements
    const brandFilter = document.getElementById('brand');
    const priceFilter = document.getElementById('price');
    // Get table and rows
    const table = document.getElementById('purifierTable');
    const rows = table.getElementsByTagName('tr');
    // Add event listeners to filters
    brandFilter.addEventListener('change', filterTable);
    priceFilter.addEventListener('change', filterTable);
    // Filter table based on selected options
    function filterTable() {
      const selectedBrand = brandFilter.value;
      const selectedPrice = priceFilter.value;
      for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const brand = row.getElementsByTagName('td')[0].textContent;
        const price = parseFloat(row.getElementsByTagName('td')[2].textContent.replace('$', ''));
        let brandMatch = true;
        let priceMatch = true;
        if (selectedBrand && brand !== selectedBrand) {
          brandMatch = false;
        }
        if (selectedPrice) {
          const [min, max] = selectedPrice.split('-').map(parseFloat);
          if (isNaN(max)) {
            priceMatch = price >= min;
          } else {
            priceMatch = price >= min && price <= max;
          }
        }
        if (brandMatch && priceMatch) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      }
    }