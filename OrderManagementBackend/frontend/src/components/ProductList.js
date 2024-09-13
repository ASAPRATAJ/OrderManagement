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
        const response = await axios.get('https://ordermanagement.up.railway.app/api/products/', {
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
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-lg font-semibold">Loading products...</p>
      </div>
    ); // Komunikat podczas ładowania
  }

  if (error) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-red-500">{error}</p> {/* Komunikat błędu */}
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto p-6 bg-white shadow-md rounded-lg mt-10">
      <h1 className="text-3xl font-bold mb-6 text-center">Product List</h1>
      {products.length === 0 ? (
        <p className="text-center">No products available.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {products.map((product) => (
            <div
              key={product.id}
              className="border border-gray-300 rounded-lg p-4 hover:shadow-lg transition duration-300"
            >
              <img
                src={product.image} // Backend zawsze dostarcza obraz, czy to domyślny, czy własny
                alt={product.title}
                className="w-full h-48 object-cover rounded-md mb-4"
              />
              <h3 className="text-xl font-semibold mb-2">{product.title}</h3>
              <p className="text-gray-600 mb-2">{product.description}</p>
              <p className="text-lg font-bold">{product.price} zł</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ProductList;
