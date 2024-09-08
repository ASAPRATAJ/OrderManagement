import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderCreate = () => {
  const [user, setUser] = useState('');
  const [products, setProducts] = useState([]);
  const [orderProducts, setOrderProducts] = useState([]);
  const [message, setMessage] = useState('');

  // Fetch products from the API
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/'); // Endpoint, który zwraca listę produktów
        setProducts(response.data);
        // Initialize orderProducts with empty quantities
        setOrderProducts(response.data.map(product => ({ product_id: product.id, quantity: 0 })));
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  const handleQuantityChange = (index, value) => {
    const newOrderProducts = [...orderProducts];
    newOrderProducts[index].quantity = parseInt(value);
    setOrderProducts(newOrderProducts);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      user,
      products: orderProducts.filter(product => product.quantity > 0) // Wyślemy tylko te produkty, które mają ilość większą niż 0
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/orders/create/', data); // Endpoint do tworzenia zamówienia
      setMessage('Order created successfully!');
      console.log(response.data);
    } catch (error) {
      console.error(error);
      setMessage('Error creating order.');
    }
  };

  return (
    <div>
      <h2>Create Order</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>User ID:</label>
          <input
            type="number"
            value={user}
            onChange={(e) => setUser(e.target.value)}
            required
          />
        </div>

        <h3>Products</h3>
        {products.length === 0 ? (
          <p>Loading products...</p>
        ) : (
          products.map((product, index) => (
            <div key={product.id}>
              <label>{product.title}</label> {/* Wyświetlamy nazwę produktu */}
              <input
                type="number"
                value={orderProducts[index]?.quantity || 0}
                onChange={(e) => handleQuantityChange(index, e.target.value)}
                min="0"
              />
            </div>
          ))
        )}

        <button type="submit">Create Order</button>
      </form>
    </div>
  );
};

export default OrderCreate;
