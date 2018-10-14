import {Component, OnDestroy, OnInit} from '@angular/core';
import {AppService} from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent implements OnInit, OnDestroy {
  title = 'App!!';
  msg: string;
  ioConnection: any;
  messages = [];
  messageContent: string;
  isConnected: boolean;
  clients = 0;

  constructor(private appService: AppService) {
  }

  ngOnInit() {
    this.appService.testRoute().subscribe(data => this.msg = data['msg']);
    this.initIoConnection();
  }

  ngOnDestroy() {
    this.ioConnection.unsubscribe();
  }

  private initIoConnection(): void {
    this.appService.initSocket();


    this.appService.onEvent(Event.CONNECT)
      .subscribe(() => {
        this.isConnected = true;
        console.log('connected');
      });

    this.ioConnection = this.appService.onMessage()
      .subscribe((message: any) => {
        if (message.hasOwnProperty('count')) {
          console.log('Message', message)
          this.clients = message['count'];
        } else {
          this.messages.push(message);
        }
        console.log(this.messages);
      });

    this.appService.onEvent(Event.DISCONNECT)
      .subscribe((data) => {
        this.isConnected = false;
        console.log('disconnected');
      });
  }

  public sendMessage(message: string, broadcast: boolean): void {
    if (!message) {
      return;
    }
    this.appService.send({
      from: 'user',
      content: message,
      isBroadcast: broadcast
    });
    this.messageContent = null;
  }
}

export enum Event {
  CONNECT = 'connect',
  DISCONNECT = 'disconnect'
}

