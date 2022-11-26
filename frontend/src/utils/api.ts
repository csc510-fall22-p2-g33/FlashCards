import axios, { AxiosInstance } from 'axios'

const baseURL = process.env.REACT_APP_API_URL

const http: AxiosInstance = axios.create({
  baseURL,
})

http.defaults.headers.post['Content-Type'] = 'application/json'

export default http