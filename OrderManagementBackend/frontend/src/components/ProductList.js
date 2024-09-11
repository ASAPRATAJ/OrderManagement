import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true); // Stan ładowania
  const [error, setError] = useState(null); // Stan błędu

  useEffect(() => {
    const token = localStorage.getItem('token'); // Pobieramy token z localStorage

    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/', {
          headers: {
            Authorization: `Bearer ${token}`, // Dodajemy token w nagłówkach
          },
        });
        setProducts(response.data); // Ustawiamy pobrane produkty
      } catch (error) {
        setError('There was an error fetching the products!'); // Obsługa błędów
      } finally {
        setLoading(false); // Ustawiamy koniec ładowania
      }
    };

    fetchProducts();
  }, []);

  if (loading) {
    return <div>Loading...</div>; // Komunikat podczas ładowania
  }

  if (error) {
    return <div>{error}</div>; // Komunikat błędu
  }

  return (
    <div>
      <h1>Product List</h1>
      {products.length === 0 ? (
        <p>No products available.</p>
      ) : (
        <ul>
          {products.map((product) => (
            <li key={product.id}>
              {product.title} - {product.description} - {product.price}zł
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProductList;
