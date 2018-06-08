import {Component, OnInit} from '@angular/core';
import {AppService} from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'App!!';
  msg: string;

  constructor(private appService: AppService) {
  }

  ngOnInit() {
    this.appService.testRoute().subscribe(data => this.msg = data['msg']);
  }
}
