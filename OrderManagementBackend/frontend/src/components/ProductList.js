import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/products/')
    .then((response) => {
      setProducts(response.data);
    })
    .catch((error) => {
      console.error('There was an error fetching the products!', error);
    });
  }, []);

  return (
    <div>
      <h1>Product List</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.title} - ${product.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
