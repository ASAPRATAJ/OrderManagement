import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

const OrderCreate = () => {
  const [products, setProducts] = useState([]);
  const [orderProducts, setOrderProducts] = useState([]);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  // Sprawdzamy, czy użytkownik jest zalogowany
  const token = localStorage.getItem('token');
  let decodedToken = null;
  let userId = null;

  if (token) {
    try {
      decodedToken = jwtDecode(token);
      userId = decodedToken.user_id;
    } catch (error) {
      console.error('Error decoding token:', error);
    }
  }

  // Jeśli token nie istnieje lub jest nieprawidłowy, przekierowujemy na stronę logowania
  useEffect(() => {
    if (!token) {
      navigate('/login'); // Przekierowanie do strony logowania
    }
  }, [token, navigate]);

  // Fetch products from the API
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/', {
          headers: {
            Authorization: `Bearer ${token}`, // Dodajemy token w nagłówku
          },
        });
        setProducts(response.data);
        // Initialize orderProducts with empty quantities
        setOrderProducts(response.data.map(product => ({ product_id: product.id, quantity: 0 })));
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    if (token) {
      fetchProducts();
    }
  }, [token]);

  const handleQuantityChange = (index, value) => {
    const newOrderProducts = [...orderProducts];
    newOrderProducts[index].quantity = parseInt(value);
    setOrderProducts(newOrderProducts);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      user: userId,
      products: orderProducts.filter(product => product.quantity > 0), // Wyślemy tylko te produkty, które mają ilość większą niż 0
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/orders/create/', data, {
        headers: {
          Authorization: `Bearer ${token}`, // Token w nagłówku
        },
      });
      setMessage('Order created successfully!');
      console.log(response.data);
    } catch (error) {
      console.error(error);
      setMessage('Error creating order.');
    }
  };

  // Jeśli użytkownik nie jest zalogowany, nie wyświetlamy formularza
  if (!token) {
    return <p>You must be logged in to create an order.</p>;
  }

  return (
    <div>
      <h2>Create Order</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
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
