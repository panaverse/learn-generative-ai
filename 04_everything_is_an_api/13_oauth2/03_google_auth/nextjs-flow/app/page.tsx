"use client"
/**
 * v0 by Vercel.
 * @see https://v0.dev/t/yYByZhG29TC
 */
import { Button } from "@/components/ui/button"

export default function Component() {

  const googleRedirect = () => {
    window.location.href = `http://localhost:8000/api/google/login`;
  };

  return (
    <div className="flex flex-col bg-gray-900 items-center justify-center min-h-screen bg-gray-100 dark:bg-gray-900">
      <Button onClick={googleRedirect} className="w-full max-w-sm" variant="outline">
        <ChromeIcon className="h-5 w-5 mr-2" />
        Sign in with Google
      </Button>
    </div>
  )
}

function ChromeIcon(props: any) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
      <circle cx="12" cy="12" r="4" />
      <line x1="21.17" x2="12" y1="8" y2="8" />
      <line x1="3.95" x2="8.54" y1="6.06" y2="14" />
      <line x1="10.88" x2="15.46" y1="21.94" y2="14" />
    </svg>
  )
}
