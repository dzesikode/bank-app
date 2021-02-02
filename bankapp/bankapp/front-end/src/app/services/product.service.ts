import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Product } from '../model/product';

const BASE_URL = 'api/products';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  // TODO: Add error handling

  readAll(): Observable<Product[]> {
    return this.http.get<Product[]>(`products`);
  }

  read(productName: string): Observable<Product> {
    return this.http.get<Product>(`${BASE_URL}/${productName}`);
  }

  create(product: Product): Observable<Product> {
    return this.http.post<Product>(`${BASE_URL}/manage/add`, product, this.httpOptions);
  }

  update(product: Product, productName: string): Observable<any> {
    return this.http.put(`${BASE_URL}/manage/${productName}`, product, this.httpOptions);
  }

  delete(product: Product, productName: string): Observable<any> {
    return this.http.delete(`${BASE_URL}/manage/${productName}`, this.httpOptions);
  }

  searchByCriteria(ageBracket: string, incomeBracket: string, student: boolean): Observable<any> {
    return this.http.get(`${BASE_URL}/search?ageBracket=${ageBracket}&incomeBracket=${incomeBracket}&student=${student}`,
      this.httpOptions);
  }
}