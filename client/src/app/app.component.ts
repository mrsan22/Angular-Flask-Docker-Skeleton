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
  ioConnection: any;
  messages = [];
  action = Action;
  user: User;
  messageContent: string;

  constructor(private appService: AppService) {
  }

  ngOnInit() {
    this.appService.testRoute().subscribe(data => this.msg = data['msg']);
    this.initIoConnection();
  }

  private initIoConnection(): void {
    this.appService.initSocket();

    this.ioConnection = this.appService.onMessage()
      .subscribe((message: any) => {
        this.messages.push(message);
        console.log(this.messages);
      });

    this.appService.onEvent(Event.CONNECT)
      .subscribe(() => {
        console.log('connected');
      });

    this.appService.onEvent(Event.DISCONNECT)
      .subscribe(() => {
        console.log('disconnected');
      });
  }

  public sendMessage(message: string): void {
    if (!message) {
      return;
    }

    this.appService.send({
      from: this.user,
      content: message
    });
    this.messageContent = null;
  }

  public sendNotification(params: any, action: Action): void {
    let message;

    if (action === Action.JOINED) {
      message = {
        from: this.user,
        action: action
      }
    } else if (action === Action.RENAME) {
      message = {
        action: action,
        content: {
          username: this.user.name,
          previousUsername: params.previousUsername
        }
      };
    }

    this.appService.send(message);
  }
}

export enum Event {
  CONNECT = 'connect',
  DISCONNECT = 'disconnect'
}

export enum Action {
  JOINED,
  LEFT,
  RENAME
}

export interface User {
  id?: number;
  name?: string;
  avatar?: string;
}
