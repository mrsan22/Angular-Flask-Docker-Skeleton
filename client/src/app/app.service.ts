import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import { Observable } from 'rxjs';
import * as socketIo from 'socket.io-client';

  export enum Event {
      CONNECT = 'connect',
      DISCONNECT = 'disconnect'
  }

@Injectable()
export class AppService {
  constructor(private http: HttpClient) {
  }

  private socket;

  public initSocket(): void {
    this.socket = socketIo('/websocket_test');
  }

  public send(message: any): void {
    console.log('Msg',message);
    this.socket.emit('message', message);
  }

  public onMessage(): Observable<any> {
    return new Observable<any>(observer => {
      this.socket.on('message', (data: any) => observer.next(data));
    });
  }

  public onEvent(event: Event): Observable<any> {
    return new Observable<Event>(observer => {
      this.socket.on(event, () => observer.next());
    });
  }

  testRoute() {
    return this.http.get('/api/ping');
  }

}
