// One runtime per page. A scene change sends a message; it does not boot another player.
let instance, starting;
export function bootUnity(canvas, config, onProgress) {
  if (instance) return Promise.resolve(instance);
  if (starting) return starting;
  starting = new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = config.loaderUrl;
    script.onerror = () => reject(new Error('Unity loader를 다운로드하지 못했습니다.'));
    script.onload = () => {
      if (typeof window.createUnityInstance !== 'function') return reject(new Error('Unity loader 형식 오류'));
      window.createUnityInstance(canvas, config.playerConfig, onProgress).then(value => {
        instance = value; resolve(value);
      }, reject);
    };
    document.body.append(script);
  });
  return starting;
}
export function openScene(player, sceneId, contentVersion) {
  const requestId = crypto.randomUUID();
  player.SendMessage('SceneBridge', 'OpenScene', JSON.stringify({sceneId, contentVersion, requestId}));
  return requestId;
}
export async function quitUnity() {
  if (instance) { await instance.Quit(); instance = null; starting = null; }
}
