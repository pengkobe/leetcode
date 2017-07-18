1. 清晰版 -> 清新版
2. 错误处理
```javascript
case -10002:
    myNote.myNotice('说话时间太短！' );
    break;
case 22406:
    myNote.myNotice('您不在当前群组当中！' );
```
3. 图片清晰度
    ChatUtilService
    ChatCtrl
        quality: 100,
        targetWidth: 720,
        targetHeight: 720,

4. 群组显示 ID
```javascript
if(sendUserId == self.id){
    return self;
}
```

5. 默认为消息 TAB contactCtrl
   > $scope.currentFeedsType = 'messagetab';
  
6. 
> .rj-message-wrap .rj-head-pic-right {
  height: 40px;
  width: 40px;
}

7. alert('相册取照片出错了！！' + err);
   > myNote.myNotice("从相册获取照片失败！！");

8. 编辑头像用不了，但是拍照是可以指定截取大小的

9. 将通讯录中的字体加大

9. 
mediaRec1 Media_duration: -1_position: -1errorCallback: (e)id: "ec40b53d-7c64-622e-3594-9f3e03974e5a"src: "file:///storage/emulated/0/Android/data/com.ionicframework.mode356491/cordovaIMVoice.amr"statusCallback: undefinedsuccessCallback: (e)arguments: nullcaller: nulllength: 1name: ""prototype: Object__proto__: ()<function scope>__proto__: Object
all.js:3 touchend():Audio Error: 1
all.js:3 touchend():Audio Error: 0
all.js:1 android leave
all.js:1 android enter
all.js:1 android leave
all.js:1 android enter
all.js:3 mediaRec1 Media_duration: -1_position: -1errorCallback: (e)id: "4262d275-4e9f-4633-95ba-8b2bbbb5b465"src: "file:///storage/emulated/0/Android/data/com.ionicframework.mode356491/cordovaIMVoice.amr"statusCallback: undefinedsuccessCallback: (e)__proto__: Object
all.js:3 录音失败执行函数 startRec
all.js:3 Object
all.js:3 touchend():Audio Success
all.js:3 touchend():Audio Error: -2147483648
all.js:3 mediaRec1 Media
all.js:3 录音失败执行函数 startRec
all.js:3 Objectcode: 1__proto__: Object
all.js:3 touchend():Audio Success
all.js:3 touchend():Audio Error: -2147483648

I/HwMediaRecorderImpl: checkRecordActive
E/MediaRecorder: start failed: -38
W/System.err: java.lang.IllegalStateException
W/System.err:     at android.media.MediaRecorder.native_start(Native Method)
W/System.err:     at android.media.MediaRecorder.start(MediaRecorder.java:1157)
W/System.err:     at org.apache.cordova.media.AudioPlayer.startRecording(AudioPlayer.java:162)
W/System.err:     at org.apache.cordova.media.AudioHandler.startRecordingAudio(AudioHandler.java:287)
W/System.err:     at org.apache.cordova.media.AudioHandler.promptForRecord(AudioHandler.java:543)
W/System.err:     at org.apache.cordova.media.AudioHandler.execute(AudioHandler.java:118)
W/System.err:     at org.apache.cordova.CordovaPlugin.execute(CordovaPlugin.java:98)
W/System.err:     at org.apache.cordova.PluginManager.exec(PluginManager.java:132)
W/System.err:     at org.apache.cordova.CordovaBridge.jsExec(CordovaBridge.java:57)
W/System.err:     at org.apache.cordova.engine.SystemExposedJsApi.exec(SystemExposedJsApi.java:41)
W/System.err:     at org.chromium.base.SystemMessageHandler.nativeDoRunLoopOnce(Native Method)
W/System.err:     at org.chromium.base.SystemMessageHandler.handleMessage(SystemMessageHandler.java:39)
W/System.err:     at android.os.Handler.dispatchMessage(Handler.java:102)
W/System.err:     at android.os.Looper.loop(Looper.java:150)
W/System.err:     at android.os.HandlerThread.run(HandlerThread.java:61)
W/PluginManager: THREAD WARNING: exec() call to Media.startRecordingAudio blocked the main thread for 80ms. Plugin should use CordovaInterface.getThreadPool().
E/AudioPlayer: FAILED renaming /storage/emulated/0/tmprecording-1500274480598.3gp to /storage/emulated/0/Android/data/com.ionicframework.mode356491/cordovaIMVoice.amr
I/MediaPlayer: setDataSource(119, 0, 576460752303423487)
I/AudioManager: requestAudioFocus() status : 1
I/AudioManager: requestAudioFocus() apk    : com.ionicframework.mode356491
W/PluginManager: THREAD WARNING: exec() call to Media.startPlayingAudio blocked the main thread for 69ms. Plugin should use CordovaInterface.getThreadPool().
I/MediaPlayer: [HSM] stayAwake true uid: 10862, pid: 10019
I/MediaPlayer: [HSM] stayAwake false uid: 10862, pid: 10019
W/MediaPlayer: Stream has no duration and is therefore not seekable.


10. this.player.prepare();



I/TDLog: onPageEnd being called! pageName: MainActivity
I/MediaPlayer: setDataSource(/storage/emulated/0//storage/emulated/0/Android/data/com.ionicframework.mode356491/cordovaIMVoice.amr)
E/MediaPlayer: error (1, -2147483648)
I/AudioManager: requestAudioFocus() status : 1
I/AudioManager: requestAudioFocus() apk    : com.ionicframework.mode356491
W/PluginManager: THREAD WARNING: exec() call to Media.startPlayingAudio blocked the main thread for 90ms. Plugin should use CordovaInterface.getThreadPool().
I/chromium: [INFO:CONSOLE(5)] "touchend():Audio Error: 1", source: file:///android_asset/www/dist/all.js (5)
I/chromium: [INFO:CONSOLE(5)] "touchend():Audio Error: 0", source: file:///android_asset/www/dist/all.js (5)
I/chromium: [INFO:CONSOLE(1)] "android leave", source: file:///android_asset/www/dist/all.js (1)
I/TDLog: New data found, Submitting...
I/TDLog: Data submitted successfully!
I/TDLog: [Session] - Same session as before!
I/TDLog: onPageEnd being called! pageName: MainActivity
I/chromium: [INFO:CONSOLE(1)] "android enter", source: file:///android_asset/www/dist/all.js (1)
I/chromium: [INFO:CONSOLE(1)] "android leave", source: file:///android_asset/www/dist/all.js (1)
I/AudioRecordPermission: remindWithResult:false
I/MediaRecorder: start
I/HwMediaRecorderImpl: HwMediaRecorderImpl
I/HwMediaRecorderImpl: checkRecordActive
I/HwMediaRecorderImpl: sendStateChangedIntent, state=3
I/TDLog: [Session] - Same session as before!
I/chromium: [INFO:CONSOLE(1)] "android enter", source: file:///android_asset/www/dist/all.js (1)
I/TDLog: No new data found!