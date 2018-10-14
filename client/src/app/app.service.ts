import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import * as socketIo from 'socket.io-client';

export enum Event {
  CONNECT = 'connect',
  DISCONNECT = 'disconnect'
}

@Injectable()
export class AppService {
  private socket;
  constructor(private http: HttpClient) {
  }

  public initSocket(): void {
    this.socket = socketIo('/websocket_test');
  }

  public send(message: any): void {
    this.socket.emit('json', {data: message});
  }

  // Event handler
  public onMessage(): Observable<any> {
    return Observable.create(observer => {
      this.socket.on('my response', msg => {
        observer.next(msg);
      });
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
