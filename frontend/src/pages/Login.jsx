import React, { useEffect } from 'react';
import Form from '../components/Form'; 

function Login() {
  useEffect(() => {
    document.body.style.overflow = 'hidden'; 
    return () => {
      document.body.style.overflow = 'auto';
    };
  }, []);

  return (
    <div className="login-page">
      <Form />
    </div>
  );
}

export default Login;