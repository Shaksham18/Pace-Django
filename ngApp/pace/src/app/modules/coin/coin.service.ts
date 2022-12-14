import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoinService {
  base_url = 'http://localhost:5000'
  constructor(
    private http: HttpClient,
  ) { }

  private getAllCoinDjangoUrl = `${this.base_url}/coin/`;
  getAllCoin() {
      return this.http.get<any>(this.getAllCoinDjangoUrl);
  }

  
}
