import { Component, OnDestroy, OnInit } from '@angular/core';
import { CoinService } from '../coin.service';

@Component({
  selector: 'app-coin',
  templateUrl: './coin.component.html',
  styleUrls: ['./coin.component.css']
})
export class CoinComponent implements OnInit,OnDestroy {
  coins = [];
  interval:any;
  constructor(
    private coinService: CoinService
  ) { }

  ngOnInit(): void {
    this.get_coin_data()
    this.interval = setInterval(() => {
      this.get_coin_data()
    },3000)
  }

  ngOnDestroy(): void {
    clearInterval(this.interval)
  }

  get_coin_data(){
    this.coinService.getAllCoin().subscribe(res => {
      let data = res.data
      for (let i = 0; i < data.length; i++) {
        data[i]['volume24h']  = data[i]['volume24h'].split(' | ')
      }
      this.coins = data
    })
  }
  
}

